from django.urls import path
from .views import *
urlpatterns=[
    path('dashboard/patient_create/',PatientCreateView.as_view(),name='patient_create'),
    path('dashboard/patient_list/',PatientListView.as_view(),name='patient_list'),
    path('dashboard/<int:pk>/patient_update',PatientUpdateView.as_view(),name='patient_update'),
    path('dashboard/<int:pk>/patient_detail',PatientDetailView.as_view(),name='patient_detail'),

    path('ajax/load-districts/', load_districts, name='ajax_load_districts'),
    path('ajax/load-muni/', load_municipalities, name='ajax_load_muni'),
    path('ajax/load-ward/', load_wards, name='ajax_load_ward'),

    path('ajax/validate_citizenship',validate_citizenshipnumber,name='validate_citizenship'),
    path('dashbaord/<int:pk>/mydeatil/',mydetail,name='mydetail'),

    path('dashboard/<int:id>/add_service',add_patient_service,name='add_service'),

]