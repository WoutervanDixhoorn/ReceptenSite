from django.contrib import admin
from . models import Ingredient, Recepten

admin.site.register(Recepten)
admin.site.register(Ingredient)