from django.urls import path
from . import views

# URL Configuration
urlpatterns = [
  path('indeed/', views.parse_search_page),
]