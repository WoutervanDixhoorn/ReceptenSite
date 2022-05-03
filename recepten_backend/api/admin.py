from django.contrib import admin
from . models import Ingredient, Recepten, User

admin.site.register(User)
admin.site.register(Recepten)
admin.site.register(Ingredient)