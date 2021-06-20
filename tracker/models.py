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
    def get_goal(self):
        return self.get_goal_display()


class BodyWeight(models.Model):
    """
    
    A Model that defines the weight of a certain user
    the foreign key allows for a one to many relationship between the user and 
    the body weight objects allowing for us to filter out all the weight entries 
    of a specific user and graphing them 
    
    """
    from users.models import Profile
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_query_name="bodyweight")
    weight = models.FloatField(max_length=4, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.user.username}'s weight on {self.date_added}"
