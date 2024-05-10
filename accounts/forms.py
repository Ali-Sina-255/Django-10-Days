from typing import Any, Mapping
from django.contrib.auth import get_user_model
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
non_allowed_username = ['ali', 'kah', 'jan']

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=244)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   id: 'user-password'}
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if username in non_allowed_username:
            raise forms.ValidationError('this is not a valid username,please pick a anther one ')
        if qs.exists():
            raise forms.ValidationError("this is not a valid username, please pick a different username")
        return username
  

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=244)
    email = forms.EmailField()
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               "id": 'user-password'
               }
    ))

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               "id": 'user-password'
               }
    ))


    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise format.ValidationError('this is already in user  please pick anther one')
        return email
    
