from django import forms
from .models import Register,Gallery

class RegisterForm(forms.ModelForm):
	Password=forms.CharField(widget=forms.PasswordInput)
	CPassword=forms.CharField(widget=forms.PasswordInput)
	class Meta():
		model=Register
		fields='__all__'

class LoginForm(forms.ModelForm):
	Password=forms.CharField(widget=forms.PasswordInput)
	class Meta():
		model=Register
		fields=('Email','Password',)

class UpdatePassword(forms.Form):
	CurrentPassword=forms.CharField(widget=forms.PasswordInput)
	NewPassword=forms.CharField(widget=forms.PasswordInput)
	CPassword=forms.CharField(widget=forms.PasswordInput)

class UpdateGallery(forms.ModelForm):
	class Meta():
		model=Gallery
		fields='__all__'

