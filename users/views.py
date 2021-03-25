from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import UserSerializer
from .models import User
# Create your views here.

class UserListCreateView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyCreateView(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'