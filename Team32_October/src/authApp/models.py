from django.db import models

# Create your models here.
class User(models.Model):
 name = models.CharField(max_length=255)
 email = models.EmailField(max_length=500, unique=True)
 username = models.CharField(max_length=255, unique=True)
 password = models.CharField(max_length=255)
 blood = models.CharField(max_length=4)
def __str__(self):
  return self.username