from tracker.models import WorkOut
from users.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import User
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