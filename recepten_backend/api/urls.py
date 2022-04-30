from urllib.parse import urlparse
from django.urls import path, include
from . views import PostsView


urlpatterns = [
    path('posts/', PostsView.as_view(), name='post_view'),
]