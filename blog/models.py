from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
