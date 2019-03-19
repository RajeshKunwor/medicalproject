from django.urls import path
from prescriptions.views import *
urlpatterns =[

    # path('dashboard/prescription_create/',PrescriptionCreateView.as_view(),name='prescription_create'),
    path('dashboard/<int:pk>/prescription_list/',PrescriptionListView.as_view(),name='prescription_list'),
    path('dashboard/<int:pk>/prescription_update',PrescriptionUpdateView.as_view(),name='prescription_update'),

    path('dashboard/<int:pk>/prescribedmedicine_create/',PrescribedMedicinesCreateView.as_view(),name='prescribedmedicine_create'),
    path('dashboard/<int:pk>/prescribedmedicine_list/',PrescribedMedicineListView.as_view(),name='prescribedmedicine_list'),

    path('load_observtion', load_observation, name='load_observation'),


]