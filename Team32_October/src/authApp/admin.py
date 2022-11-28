from django.contrib import admin
from django.urls import path, include
from .models import User, Doctor
from django.apps import apps

# Register your models here.
for model in apps.get_app_config('authApp').get_models():
    admin.site.register(model)
