from django import forms
from .models import User

"""hide password field in login form"""
passwordInputWidget = {
 'password': forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'})),
}
class RegisterForm(forms.ModelForm):
 class Meta:
  model = User
  fields = '__all__'
  widgets = [passwordInputWidget]
  widgets = {
    'username': forms.TextInput(attrs={'class': 'form-control'}),
    'email': forms.EmailInput(attrs={'class': 'form-control'}),
    'password': forms.PasswordInput(attrs={'class': 'form-control'}),
    'first_name': forms.TextInput(attrs={'class': 'form-control'}),
    'last_name': forms.TextInput(attrs={'class': 'form-control'}),
    'phone': forms.TextInput(attrs={'class': 'form-control'}),
    'blood_group': forms.TextInput(attrs={'class': 'form-control'}),
  }
class LoginForm(forms.ModelForm):
 class Meta:
  model = User
  fields = ['username', 'password']
  widgets = [passwordInputWidget]
  widgets = {
    'password': forms.PasswordInput(attrs={'class': 'form-control'}),
  }