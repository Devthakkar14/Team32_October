from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
class Document(models.Model):
    user = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')