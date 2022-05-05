import email
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from requests import post
from .utils import get_tokens_for_user
from rest_framework import permissions, serializers
from rest_framework import response
from rest_framework.response import Response
from rest_framework import generics, status
from . models import Recepten, Profile
from . serializers import ReceptenSerializer, LoginSerializer, RegisterSerializer, ProfileDetailsSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


class RegisterView(generics.GenericAPIView):
    authentication_classes = [] 
    permission_classes = [] 

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = []

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

class ProfileView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = Profile.objects.prefetch_related('user')

    def get_profile(self, username):
        try:
            return Profile.objects.filter(user__username=username)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, username):
        queryset = self.get_profile(username)
        serializer = ProfileDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

class ReceptenView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = Recepten.objects.prefetch_related('ingredienten')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ReceptenSerializer(queryset, many=True)
        return Response(serializer.data)
        