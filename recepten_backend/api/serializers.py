from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Ingredient, Recepten, User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'city', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

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