from urllib.parse import urlparse
from django.urls import path, include
from . views import ReceptenView, LoginView, LogoutView, RegisterView, ProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register', RegisterView.as_view(), name='register_view'),
    path('login', LoginView.as_view(), name='login_view'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutView.as_view(), name='logout_view'),
    path('profile/<str:username>', ProfileView.as_view(), name='profiles_view'),
    path('', ReceptenView.as_view(), name='recepten_view'),
]