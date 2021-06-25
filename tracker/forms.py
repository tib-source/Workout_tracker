from django import forms
from django.db import models
from .models import BodyWeight

class BodyWeightForm(forms.ModelForm):
    class Meta:
        model = BodyWeight
        fields = ['weight']


