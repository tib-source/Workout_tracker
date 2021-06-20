from django.contrib import admin
from .models import Contact, Profile
# Register your models here.

admin.site.register(Profile)
admin.site.register(Contact)