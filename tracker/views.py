from tracker.models import  WorkOut
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import BodyWeightForm
from django.contrib import messages
from django.views.generic import ListView


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

    context = {
        'workout':WorkOut.objects.all(),
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


def log_workout_view(request):
    context = {
        'stronglift': WorkOut.objects.first().excercise.all()
    }
    return render(request, 'tracker/log_workout.html', context )