from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class WorkOut(models.Model):
    image = models.ImageField(upload_to='media/static/workout_images', null=True, blank=True)
    name = models.CharField(max_length = 200)
    description = models.TextField(null=True, blank=True)
    def __str__(self) -> str:
        return self.name



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


