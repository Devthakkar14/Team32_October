from django.urls import include, path
from . import views
from django.urls import path, include 

app_name = 'authApp'
urlpatterns = [
 path('register/', views.register, name='register'),
 path('login/', views.login, name='login'),
 path('', views.home, name='home'),
 path('logout/', views.logout, name='logout'),
 path('ajax_generate_code/', views.ajax_generate_code, name='ajax_generate_code'),
 path("file/", include("fileupload.urls")),
]