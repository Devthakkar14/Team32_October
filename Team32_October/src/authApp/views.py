from django.shortcuts import render, redirect
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .models import Doctor
from .forms import RegisterForm, LoginForm, DoctorRegisterForm, DoctorLoginForm
from .decorators import user_login_required, doctor_login_required
import random
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from mysite.settings import EMAIL_HOST_USER
from django.http import HttpResponse, HttpResponseBadRequest

from django.shortcuts import redirect, render


razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

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

def payment(request):
    currency = 'INR'
    amount = 50000

    razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))

    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'payment.html', context=context)

@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            razorpay_payment_id = request.POST.get('razorpay_payment_id')
            razorpay_order_id = request.POST.get('razorpay_order_id')
            razorpay_signature = request.POST.get('razorpay_signature')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            }
            
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                amount = 50000
                try:
                    razorpay_client.payment.capture(razorpay_payment_id, amount)
                    return render(request, 'paymentsuccess.html')
                except:
                    return render(request, 'paymentfailure.html')
            else:
                return render(request, 'paymentfailure.html')

        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()

#create function for doctorregister
def doctorregister(request):
    form = DoctorRegisterForm()
    success = None
    if request.method=='POST':
        if Doctor.objects.filter(username=request.POST['username']).exists():
            error = "This username is already taken"
            return render(request, 'doctorregister.html', {'form': form, 'error': error})
        if Doctor.objects.filter(email=request.POST['email']).exists():
            error = "This email is already taken"
            return render(request, 'doctorregister.html', {'form': form, 'error': error})
    
        if (not 'code' in request.POST) or (not 'code' in request.session) or (not request.POST['code']==str(request.session['code'])):
            error = "Invalid Verification Code"
            return render(request, 'doctorregister.html', {'form': form, 'error': error})
        form = DoctorRegisterForm(request.POST)
        new_user = form.save(commit=False)
        new_user.save()
        success = "New User Created Successfully !"
    return render(request, 'doctorregister.html', {'form': form, 'success': success})

#doctor login
def doctorlogin(request):
 form = DoctorLoginForm()
 if request.method=='POST':
  username = request.POST['username']
  password = request.POST['password']
  if Doctor.objects.filter(username=username, password=password).exists():
   doctor = Doctor.objects.get(username=username)
   request.session['doctor_id'] = doctor.id
   if is_logged_in:
    return redirect('authApp:doctorhome')
   else:
    return redirect('authApp:waiting')
 return render(request, 'doctor_login.html', {'form': form})

@doctor_login_required
def doctorhome(request):
    doctor = Doctor.objects.get(is_logged_in = False)
    if doctor.is_logged_in == True:
        if 'doctor_id' in request.session:
            user = get_user(request)
            return render(request, 'doctorhome.html', {'user': user})
        else:
            return redirect('authApp:doctorlogin')
    else:
        return redirect('authApp:waiting')
def doctorlogout(request):
    if 'user_id' in request.session:
        del request.session['user_id'] 
    return redirect('authApp:doctorlogin')

def landing_page(request):
    return render(request, 'landing_page.html')

def waiting(request):
    return render(request, 'waiting.html')
