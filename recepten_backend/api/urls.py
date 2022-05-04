from urllib.parse import urlparse
from django.urls import path, include
from . views import ReceptenView, LoginView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login', LoginView.as_view(), name='login_view'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutView.as_view(), name='logout_view'),
    path('', ReceptenView.as_view(), name='recepten_view'),
]