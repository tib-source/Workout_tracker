from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from tracker.models import WorkOut

@receiver(signal=post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        WorkOut.objects.create(user=instance)
        Profile.objects.create(user=instance)

@receiver(signal=post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.workout.save()

    