from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from tracker.models import WorkOut

@receiver(signal=post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(signal=post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(user_logged_in)
def login_exp_gain(sender, user, **kwargs):
    user.profile.exp += 10
    print(f"{user} just gained 50exp for logging in") 
