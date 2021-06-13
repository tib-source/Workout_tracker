from django.shortcuts import render

# Create your views here.

def homeview(request):
    context = {
        'hello': 'MY NIBBBAAAA' + str(1790-190)
    }
    return render(request, 'tracker/home.html', context)