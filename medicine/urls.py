from django.urls import path
from .views import *
urlpatterns =[

    path('dashboard/medicine_create/',MedicineCreateView.as_view(),name='medicine_create'),
    path('dashboard/appointment_list/',MedicineListView.as_view(),name='medicine_list'),
    path('dashbaord/medicine_update',MedicineUpdateView.as_view(),name='medicine_update'),



]