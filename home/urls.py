from django.urls import path,include
from .views import *
urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('view_notification/', view_notification, name='view_notification'),
    ]