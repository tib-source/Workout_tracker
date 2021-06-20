from django.forms import fields, models
from .models import Contact, Profile
from django import forms


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username','email','password1','password2'
        ]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['username', 'title', 'message']
