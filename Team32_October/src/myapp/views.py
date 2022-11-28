from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
# Create your views here.

class DocumentListView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'list.html'
    context_object_name = 'documents'
    ordering = ['-uploaded_at']
    paginate_by = 5

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DocumentForm()
        return context


def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
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
    documents = Document.objects.filter(user=request.user)

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)

def product_list_view(request):
    queryset = Document.objects.filter(user=request.user)
    context = {
        'object_list': queryset
    }
    return render(request, 'doclist.html', context)

