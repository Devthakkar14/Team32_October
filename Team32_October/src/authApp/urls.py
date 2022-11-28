from django.urls import include, path
from . import views
from django.urls import path, include 

app_name = 'authApp'
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('', views.landing_page, name='landing_page'),
    path('logout/', views.logout, name='logout'),
    path('ajax_generate_code/', views.ajax_generate_code, name='ajax_generate_code'),
    path("file/", include("fileupload.urls")),
    path('payment/paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('payment/', views.payment, name='payment'),
    path('doctorregistration/', views.doctorregister, name='doctorregistration'),
    path('doctorlogin/', views.doctorlogin, name='doctorlogin'),
    path('doctorlogout/', views.doctorlogout, name='doctorlogout'),
    path('doctorhomepage/', views.doctorhome, name='doctorhomepage'),
    path('waiting/', views.waiting, name='waiting'),
    path('ajax_doctor_code/', views.ajax_doctor_code, name='ajax_doctor_code'),
    path('ajax_org_code/', views.ajax_org_code, name='ajax_organization_code'),
    path('organizationregister/', views.organization_register, name='organizationregister'),
    path('organizationlogin/', views.organization_login, name='organizationlogin'),
    path('organizationlogout/', views.organization_logout, name='organizationlogout'),
    path('organizationhome/', views.organization_home, name='organizationhome'),

]