from django.urls import path
from .views import my_view, docsls

urlpatterns = [
    path('', my_view, name='my-view'),
    path('docsls/', docsls, name='docsls'),
]