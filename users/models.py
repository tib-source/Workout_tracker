from django.db import models
from django.contrib.auth.models import User
import bisect
import datetime

 #### LEVEL SYSTEM ####
BASE_EXP = 100
INCREASE_FACTOR = 5
LEVEL_RANGE = [BASE_EXP*(INCREASE_FACTOR*x) for x in range(50)]



class Profile(models.Model):

    GOAL_CHOICES = [
        ('LW','Loosing Weight'),
        ('GM','Gaining Muscle')
    ]
    #### MODEL FIELDS ###
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, default='Gaining Muscle')
    image = models.ImageField(default='/static/profile_pics/default.png', upload_to='media/static/profile_pics')
    exp = models.IntegerField(default=0)
    weight = models.ManyToManyField("tracker.BodyWeight")
    height = models.IntegerField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.user.username} Profile'

    @property
    def get_level(self) -> int: 
        """ 
        Takes in an int(experience ponit) and
         calculates what level a user should be 
        """
        EXP = self.exp
        level = bisect.bisect(LEVEL_RANGE, EXP)
        return level
    
    @property
    def fullname(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_level_percentage(self) -> int:
        """
        calculated the percentage of completion to the next level 
        eg -
         level 1 = 100exp
         level 2 = 200exp
        current exp = 120exp 
        next_level = 2 
        percentage_to_next_lvl = (120/200)*100 -> 60%

        """
        current_lvl = self.get_level
        current_lvl_min_exp = LEVEL_RANGE[current_lvl-1]
        current_exp = self.exp
        next_lvl_exp = LEVEL_RANGE[self.get_level+1] # "2" because the list starts at index 0 and +1 would return the exp required for the current level 
        exp = current_exp - current_lvl_min_exp
        next = next_lvl_exp - current_lvl_min_exp
        percentage = (exp/next)*100
        return percentage

    @property
    def next_level(self)-> int:
        """ returns exp reqiired for the next level"""
        return int(LEVEL_RANGE[self.get_level+1])

    @property
    def get_weight_list(self)-> tuple:
        """
        returns a list of weight objects that are linked to this profile
        """
        weight_objects = self.weight.all()
        weights = [ x.weight for x in weight_objects]
        date = [datetime.datetime.strftime(x.date_added, r'%m-%d') for x in weight_objects]
        return (weights, date)

    @property
    def get_goal(self):
        return self.get_goal_display()
        
class Contact(models.Model):
    username = models.CharField(max_length=15, null=True, default=None)
    email = models.EmailField(null=True)
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.username} -> {self.title}"
