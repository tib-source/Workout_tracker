from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GOAL_CHOICES = [
    ('LW','Loosing Weight'),
    ('GM','Gaining Muscle')
]
class WorkOut(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, default='Gaining Muscle')

    def __str__(self) -> str:
        return f"{self.user.username}'s Workout"

    @property
    def get_goals(self):
        return [x[1] for x in GOAL_CHOICES]