from django.contrib import admin
from . models import Ingredient, Recepten, User, Profile

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Recepten)
admin.site.register(Ingredient)