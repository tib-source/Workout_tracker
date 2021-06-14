from django.db import models

# Create your models here.
GOAL_CHOICES = [
    ('LW','Loosing Weight'),
    ('GM','Gaining Muscle')
]
class WorkOut(models.Model):
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, default='Gaining Muscle')
