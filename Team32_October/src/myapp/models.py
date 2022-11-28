from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Document(models.Model):
    user = models.ForeignKey(User, default = 1, null = True, on_delete = models.SET_NULL)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')