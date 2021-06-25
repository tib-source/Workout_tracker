from django.forms import fields, models
from .models import Contact, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
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
        fields = ['username', 'email','title', 'message']

class RegistrationForm(UserCreationForm):

    GOAL_CHOICES = [
    ('LW','Loosing Weight'),
    ('GM','Gaining Muscle')
    ]
    age = fields.IntegerField()
    goal = fields.ChoiceField(choices=GOAL_CHOICES)

    class Meta:
        model = User
        fields = ('last_name','first_name','username','email','age', 'goal', 'password1','password2')