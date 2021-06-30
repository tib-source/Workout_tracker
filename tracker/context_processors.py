from django.contrib.auth.models import User

def get_ranking(request):
    """
    This context processor is used to display the ranking information of users interms of exp
    """
    context = {
        'ranking': User.objects.all().order_by('-profile__exp'),
    }

    return context