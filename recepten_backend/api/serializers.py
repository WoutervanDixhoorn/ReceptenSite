from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Ingredient, Recepten, User

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'first_name', 'last_name', 'birth_date', 'address', 'city', 'about_me']
        read_only_fields = ['email', ]

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'amount', 'unit']

class ReceptenSerializer(serializers.ModelSerializer):
    ingredienten = IngredientSerializer(many=True)

    class Meta:
        model = Recepten
        fields = '__all__'