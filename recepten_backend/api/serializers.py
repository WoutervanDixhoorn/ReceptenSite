from dataclasses import field
from rest_framework import serializers
from .models import Ingredient, Recepten

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'amount', 'unit']

class ReceptenSerializer(serializers.ModelSerializer):
    ingredienten = IngredientSerializer(many=True)

    class Meta:
        model = Recepten
        fields = '__all__'