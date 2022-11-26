from django.shortcuts import render, HttpResponse
from .models import fileupload
# Create your views here.
def home(request):
    if request.method == "POST":
        file1 = request.FILES["file"]
        document = fileupload.objects.create(file=file1)
        document.save()
        return HttpResponse("File Uploaded")
    return render(request, "index.html")
