from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.UserListCreateView.as_view()),
    path('<int:id>', views.UserRetrieveUpdateDestroyCreateView.as_view())
]