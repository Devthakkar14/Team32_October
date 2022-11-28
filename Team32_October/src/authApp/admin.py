from django.contrib import admin
from django.urls import path, include
from .models import User, Doctor

# Register your models here.
admin.site.register(User)
admin.site.register(Doctor)