from dataclasses import field
from rest_framework import serializers
from .models import Recepten

class ReceptenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepten
        fields = '__all__'