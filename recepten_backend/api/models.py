from pyexpat import model
from django.db import models

# Create your models here.

# class User(models.Model):
#     username

class Recepten (models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title