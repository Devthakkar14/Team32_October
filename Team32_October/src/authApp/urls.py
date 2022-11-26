from django.urls import path
from . import views
app_name = 'authApp'
urlpatterns = [
 path('register/', views.register, name='register'),
 path('login/', views.login, name='login'),
 path('', views.home, name='home'),
 path('logout/', views.logout, name='logout'),
 path('ajax_generate_code/', views.ajax_generate_code, name='ajax_generate_code'),
]