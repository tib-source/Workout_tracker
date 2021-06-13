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
            return redirect('dashboard') ### YOU NEED TO MAKE A DASHBOARD 
        else:
            form = UserCreationForm()
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'user/register.html', context)

@login_required
def dashboard(request):
    
    return render(request, 'user/dashboard.html', context)
