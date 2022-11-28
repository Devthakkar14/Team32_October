from django import forms
from .models import User
from .models import Doctor
from .models import Organization

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

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

class LoginForm(forms.ModelForm):
 class Meta:
  model = User
  fields = ['username', 'password']
  widgets = [passwordInputWidget]
  widgets = {
    'password': forms.PasswordInput(attrs={'class': 'form-control'}),
  }

#create class for doctor
class DoctorRegisterForm(forms.ModelForm):
  class Meta:
    model = Doctor
    fields = ['name', 'email','username', 'password', 'department']
    widgets = [passwordInputWidget]
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'username': forms.TextInput(attrs={'class': 'form-control'}),
      'password': forms.PasswordInput(attrs={'class': 'form-control'}),
      'department': forms.TextInput(attrs={'class': 'form-control'}),
    }

class DoctorLoginForm(forms.ModelForm):
  class Meta:
    model = Doctor
    fields = ['username', 'password']
    widgets = [passwordInputWidget]
    widgets = {
      'password': forms.PasswordInput(attrs={'class': 'form-control'}),
    }

class OrganizationRegisterForm(forms.ModelForm):
  class Meta:
    model = Organization
    fields = ['name', 'email','username', 'password', 'Organization_Type']
    widgets = [passwordInputWidget]
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'username': forms.TextInput(attrs={'class': 'form-control'}),
      'password': forms.PasswordInput(attrs={'class': 'form-control'}),
      'Organization_Type': forms.TextInput(attrs={'class': 'form-control'}),
    }

class OrganizationLoginForm(forms.ModelForm):
  class Meta:
    model = Organization
    fields = ['username', 'password']
    widgets = [passwordInputWidget]
    widgets = {
      'password': forms.PasswordInput(attrs={'class': 'form-control'}),
    }


