from users.models import Profile
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField
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
    weight = models.FloatField(max_length=4, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"BodyWeight Object - {self.date_added}"


class WorkoutWeight(models.Model):
    """
    
    A Model that defines the weight of a certain user
    the foreign key allows for a one to many relationship between the user and 
    the body weight objects allowing for us to filter out all the weight entries 
    of a specific user and graphing them 
    
    """
    weight = models.FloatField(max_length=4, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"WorkoutWeight Object - {self.date_added}"

class Excercise(models.Model):
    """
    A model that defines a specific excercise 
    """
    name = models.CharField(max_length=100, null=True)
    weight = models.ManyToManyField(WorkoutWeight)
    set1 = models.IntegerField()
    set2 = models.IntegerField()
    set3 = models.IntegerField()
    rep_set1 = models.IntegerField()
    rep_set2 = models.IntegerField()
    rep_set3 = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Routine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    workouts = models.ManyToManyField(Excercise)

    def __str__(self) -> str:
        return self.name


