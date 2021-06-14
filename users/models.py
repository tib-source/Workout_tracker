from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='static/profile_pics')
    exp = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f'{self.user.username} Profile'