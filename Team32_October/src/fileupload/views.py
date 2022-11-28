from django.shortcuts import render, HttpResponse
from .models import fileupload
from django.shortcuts import render, redirect
# Create your views here.
def home(request):
    if request.method == "POST":
        file1 = request.FILES["file"]
        document = fileupload.objects.create(file=file1)
        document.save()
        return redirect('authApp:home')

    #load documents for the list page
    fileuploads = fileupload.objects.all()
    return render(request, "index.html")

