from typing import ContextManager
from django.shortcuts import redirect, render
from .form import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

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


