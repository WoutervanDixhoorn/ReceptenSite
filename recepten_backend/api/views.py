from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics
from . models import Posts
from . serializers import PostSerializer

def HelloWorld():
    return JsonResponse({"message":"HelloWorld"})

class PostsView(generics.RetrieveAPIView):
    queryset = Posts.objects.all();

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
        