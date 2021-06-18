from django.db import models
from django.contrib.auth.models import User
import bisect

class Profile(models.Model):
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
        EXP = getattr(self.exp)
        BASE_EXP = 200
        INCREASE_FACTOR = 2.6
        LEVEL_RANGE = [BASE_EXP+(x**INCREASE_FACTOR) for x in range(50)]
        level = bisect.bisect(LEVEL_RANGE, self.exp)
        return level
    
    @property
    def fullname(self):
        if self.firstname and self.lastname:
            return f"{self.firstname} {self.lastname}"
        else:
            return self.user.username