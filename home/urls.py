from django.urls import path,include
from .views import *
urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    ]