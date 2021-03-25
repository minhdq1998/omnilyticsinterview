from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.PostListCreateView.as_view()),
    path('<int:id>',views.PostRetrieveDestroyView.as_view())
]