from django.urls import path
from .views import *




urlpatterns = [
    path('', home, name='home'),
    path('about/<int:pk>/', about_detail, name='about_detail'),
]