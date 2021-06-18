from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.

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
        
    }
    return render(request, 'tracker/dashboard.html', context)