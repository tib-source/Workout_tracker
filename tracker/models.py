from django.db import models
# Create your models here.

class WorkOut(models.Model):
    image = models.ImageField(upload_to='media/static/workout_images', null=True, blank=True)
    name = models.CharField(max_length = 200)
    description = models.TextField(null=True, blank=True)
    excercise = models.ManyToManyField('Excercise')
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
        return f"BodyWeight Object - {self.weight}"


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
        return f"Workout Weight - {self.weight}"


    
class Excercise(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Workout_data(models.Model):
    """
    A model that defines a specific excercise 
    """
    name = models.ForeignKey(Excercise, on_delete=models.CASCADE)
    weight = models.ManyToManyField(WorkoutWeight)
    rep_set1 = models.IntegerField(default=0)
    rep_set2 = models.IntegerField(default=0)
    rep_set3 = models.IntegerField(default=0)
    filled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name.name} data"


# class Routine(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     workouts = models.ManyToManyField(Excercise)

#     def __str__(self) -> str:
#         return self.name


