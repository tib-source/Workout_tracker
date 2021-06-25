from tracker.models import Routine, WorkOut
from users.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import User
from .forms import BodyWeightForm
from django.contrib import messages
from django.views.generic import ListView, UpdateView  
def homeview(request):
    if request.user.is_authenticated:
        """
        If the user is authenticated,  
        no need to send them to landing page so they are redirected to the dashboard
        """
        return redirect('dashboard') #### 

    context = {
        'hello': 'MY NIBBBAAAA' + str(1790-190)
    }
    return render(request, 'tracker/home.html', context)



@login_required(login_url='login')
def dashboard_view(request):
    """
    ranking context -  is a list of all the users in the database ordered by the ammount of exp they have 
    This context is used for the right sidebar where a table of users is displayed and to add a competitive nature to the website
    """
    context = {
        'workout':WorkOut.objects.all(),
        'ranking': User.objects.all().order_by('-profile__exp'), 
    }
    return render(request, 'tracker/dashboard.html', context)


def weight_view(request):
    if request.POST:
        form = BodyWeightForm(request.POST)
        if form.is_valid():
            form.save()
            model_instance = form.instance
            request.user.profile.weight.add(model_instance)
            messages.success(request,'Weight successfully logged')
    else:
        form = BodyWeightForm()
    context = {}
    return render(request, 'tracker/weight.html', context)  


class WorkoutView(ListView):
    model = WorkOut
    template_name = "tracker/workout.html"