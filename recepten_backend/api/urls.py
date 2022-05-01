from urllib.parse import urlparse
from django.urls import path, include
from . views import ReceptenView


urlpatterns = [
    path('recepten/', ReceptenView.as_view(), name='recepten_view'),
]