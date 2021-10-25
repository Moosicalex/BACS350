from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Sign Up
    path('signup/', SignUpView.as_view(), name='signup'),
]