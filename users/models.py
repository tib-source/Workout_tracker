from django.db import models
from django.contrib.auth.models import User
import bisect

 #### LEVEL SYSTEM ####
BASE_EXP = 100
INCREASE_FACTOR = 5
LEVEL_RANGE = [BASE_EXP*(INCREASE_FACTOR*x) for x in range(50)]



class Profile(models.Model):

    #### MODEL FIELDS ###
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    image = models.ImageField(default='/static/profile_pics/default.png', upload_to='media/static/profile_pics')
    exp = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    
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
        if self.firstname and self.lastname:
            return f"{self.firstname} {self.lastname}"
        else:
            return self.user.username

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
        exp_current = self.exp
        current_lvl = self.get_level
        next_lvl = current_lvl + 1
        exp_for_next_lvl = LEVEL_RANGE[next_lvl]
        percentage_to_next_lvl = (exp_current/exp_for_next_lvl) * 100
        return percentage_to_next_lvl

    @property
    def next_level(self)-> int:
        """ returns exp reqiired for the next level"""
        return int(LEVEL_RANGE[self.get_level+1])