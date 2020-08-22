from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['customer','product','status']


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']