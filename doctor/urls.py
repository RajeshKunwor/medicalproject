from django.urls import path
from .views import *
urlpatterns =[
    path('dashboard/doctor_create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('dashboard/doctor_list/', DoctorListView.as_view(), name='doctor_list'),
    path('dashbaord/<int:pk>/doctor_update/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('dashboard/<int:pk>/doctor_info',DoctorDetailView.as_view(),name='doctor_info'),
    path('dashbaord/<int:pk>/doctor_detail/', mydetail, name='doctor_detail'),

    path('ajax/load-districts/', load_districts, name='ajax_load_districts'),
    path('ajax/validate_citizenship',validate_citizenshipnumber,name='validate_citizenship'),
    path('ajax/load-muni/', load_municipalities, name='ajax_load_muni'),
    path('ajax/load-ward/', load_wards, name='ajax_load_ward'),


    path('dashboard/<int:pk>/doctor_schedule_create/',DoctorScheduleCreateView.as_view(),name='doctor_schedule_create'),
    path('dashboard/<int:pk>/doctor_schedule_list/',DoctorScheduleListView.as_view(),name='doctor_schedule_list'),
    path('dashboard/<int:pk>/doctor_schedule_update',DoctorScheduleUpdateView.as_view(),name='doctor_schedule_update'),

]