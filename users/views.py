from typing import ContextManager
from users.models import Contact
from django.shortcuts import redirect, render
from .form import ContactForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.

def loginView(request):
    context = {}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid username or password')
    return render(request, 'users/login.html', context)

def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') ### YOU NEED TO MAKE A DASHBOARD 
        else:
            form = UserCreationForm()
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)


def contact_view(request):
    context = {}
    if request.POST: 
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You message has been sent')
            render(request, 'users/contact.html', context)
    form = ContactForm()
    return render(request, 'users/contact.html', context)