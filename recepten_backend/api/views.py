from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics
from . models import Recepten
from . serializers import ReceptenSerializer

class ReceptenView(generics.RetrieveAPIView):
    queryset = Recepten.objects.all();

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ReceptenSerializer(queryset, many=True)
        return Response(serializer.data)
        