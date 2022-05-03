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

class Ingredient (models.Model):
    recept = models.ForeignKey(Recepten, related_name='ingredienten', on_delete=models.DO_NOTHING)

    name = models.CharField(max_length=50)
    amount = models.IntegerField();
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.name