from django import forms
from django.contrib.auth.forms import UserCreationForm
from Auth.models import DRCUser

class createUserForm(UserCreationForm):
    class Meta:
        model = DRCUser
        fields = ['username','email', 'Phone_number', 'password1', 'password2']
