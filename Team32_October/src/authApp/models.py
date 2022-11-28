from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

    
class User(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, default = 1, null = True, on_delete = models.SET_NULL)
    email = models.EmailField(max_length=500, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    blood = models.CharField(max_length=4)

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)



def __str__(self):
  return self.username