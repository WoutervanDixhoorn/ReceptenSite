from urllib.parse import urlparse
from django.urls import path, include
from . views import ReceptenView, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login', LoginView.as_view(), name='login_view'),
    #path('login-refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', ReceptenView.as_view(), name='recepten_view'),
]