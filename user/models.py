from PIL import Image
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(default='New User', max_length=150)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    about = models.TextField(default='', max_length=250)

    def __str__(self):
        return f'{self.user.username} Profile'

