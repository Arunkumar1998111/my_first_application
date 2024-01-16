from django import forms
from django.contrib.auth.models import User


class Signupform(forms.Form):
     username = forms.CharField(label="Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg my-3'}))
     email = forms.EmailField(label="email", max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg my-3'}))
     password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg my-3'})) 
     def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken")
        return username
     

class Signinform(forms.Form):
         username = forms.CharField(label="Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg my-3'}))
         password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg my-3'})) 