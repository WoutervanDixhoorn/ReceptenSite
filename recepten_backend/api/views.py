from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from requests import post
from .utils import get_tokens_for_user
from rest_framework import permissions, serializers
from rest_framework import response
from rest_framework.response import Response
from rest_framework import generics, status
from . models import Recepten
from . serializers import ReceptenSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


class LoginView(generics.GenericAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    serializer_class = LoginSerializer

    def post(self, request):
        if 'username' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        logout(request=request)


class ReceptenView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = Recepten.objects.prefetch_related('ingredienten');

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ReceptenSerializer(queryset, many=True)
        return Response(serializer.data)
        