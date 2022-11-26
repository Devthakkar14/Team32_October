from django import forms
from .models import User
passwordInputWidget = {
 'password': forms.PasswordInput(),
}
class RegisterForm(forms.ModelForm):
 class Meta:
  model = User
  fields = '__all__'
  widgets = [passwordInputWidget]
class LoginForm(forms.ModelForm):
 class Meta:
  model = User
  fields = ['username', 'password']
  widgets = [passwordInputWidget]