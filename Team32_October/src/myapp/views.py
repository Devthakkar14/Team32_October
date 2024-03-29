from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
# Create your views here.


def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            form.user = request.user
            if form.is_valid():
                newdoc = Document(docfile=request.FILES['docfile'])
                newdoc.user = request.user;
                newdoc.save()

                # Redirect to the document list after POST
                return redirect('my-view')
            else:
                message = 'The form is not valid. Fix the following error:'
        else:
            form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    if request.user.is_authenticated:
        documents = Document.objects.filter(user=request.user)
        # Render list page with the documents and the form
        context = {'documents': documents, 'form': form, 'message': message}
        return render(request, 'list.html', context)
    else:
        return render(request, 'list.html', {'message': message})


def docsls(request):
    queryset = Document.objects.filter(user=request.user)
    context = {
        'object_list': queryset
    }
    return render(request, 'doclist.html', context)

