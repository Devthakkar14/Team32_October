from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm, LoginForm
from .decorators import user_login_required
import random
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from mysite.settings import EMAIL_HOST_USER
from django.http import HttpResponse

@user_login_required
def home(request):
 user = get_user(request)
 return render(request, 'home.html', {'user': user})

def ajax_generate_code(request):
    print(request.GET)
    for x in request.GET:
        if x!='_':
            email = x
            request.session['code'] = random.randint(100000, 999999)
            text_content = "Your Email Verification Code is " + str(request.session['code'])
            msg = EmailMultiAlternatives('Verify Email', text_content, EMAIL_HOST_USER, [email])
            msg.send()
    return HttpResponse("success")

def register(request):
    form = RegisterForm()
    success = None
    if request.method=='POST':
        if User.objects.filter(username=request.POST['username']).exists():
            error = "This username is already taken"
            return render(request, 'register.html', {'form': form, 'error': error})
        if User.objects.filter(email=request.POST['email']).exists():
            error = "This email is already taken"
            return render(request, 'register.html', {'form': form, 'error': error})
    
        if (not 'code' in request.POST) or (not 'code' in request.session) or (not request.POST['code']==str(request.session['code'])):
            error = "Invalid Verification Code"
            return render(request, 'register.html', {'form': form, 'error': error})
        form = RegisterForm(request.POST)
        new_user = form.save(commit=False)
        new_user.save()
        success = "New User Created Successfully !"
    return render(request, 'register.html', {'form': form, 'success': success})

def login(request):
 form = LoginForm()
 if request.method=='POST':
  username = request.POST['username']
  password = request.POST['password']
  if User.objects.filter(username=username, password=password).exists():
   user = User.objects.get(username=username)
   request.session['user_id'] = user.id
   return redirect('authApp:home')
 return render(request, 'login.html', {'form': form})

def get_user(request):
 return User.objects.get(id=request.session['user_id'])

def home(request):
 if 'user_id' in request.session:
  user = get_user(request)
  return render(request, 'home.html', {'user': user})
 else:
  return redirect('authApp:login')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id'] 
    return redirect('authApp:login')