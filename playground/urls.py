# map url to view
from django.urls import path
from .views import hello_view

# URL Configuration
urlpatterns = [
    path('hello/', hello_view, name='hello_view'),
]