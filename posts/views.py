from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import PostSerializer
from .models import Post
# Create your views here.

class PostListCreateView(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveDestroyView(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    
