from django.urls import path
from .views import *
urlpatterns =[

    path('dashboard/appointment_create/',AppointmentCreateView.as_view(),name='appointment_create'),
    path('dashboard/appointment_list/',AppointmentListView.as_view(),name='appointment_list'),
    path('dashbaord/appointment_update',AppointmentUpdateView.as_view(),name='appointment_update'),





]