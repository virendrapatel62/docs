from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnails/')

    def __str__(self):
        return self.title
