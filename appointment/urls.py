from django.urls import path
from .views import *
urlpatterns =[

    path('dashboard/appointment_create/',AppointmentCreateView.as_view(),name='appointment_create'),
    path('dashboard/<int:pk>/appointment_list/',AppointmentListView.as_view(),name='appointment_list'),
    path('dashboard/<int:pk>/appointment_update',AppointmentUpdateView.as_view(),name='appointment_update'),

    path('load_schedule',load_schedule,name='load_schedule'),
    path('check_appoinment',check_appointment,name='check_appointment'),
    path('check_max_patient',check_max_patient,name='check_max_patient'),

    path('dashboard/patient/<int:pk>/request_appointment/', RequestAppointment.as_view(), name="request_appointment"),
    path('dashboard/patient/<int:pk>/myappointment/', MyAppointment.as_view(), name="myappointment"),

    path('dashboard/appointment/new_appointment', NewAppointment.as_view(), name="new_appointment"),

    path('dashboard/appointment/<int:pk>/confirm_appoinment', confirm_appointment, name="comfirm_appointment"),
    path('dashboard/appointment/<int:pk>/reject_appoinment', reject_appointment, name="reject_appointment"),

    path('dashboard/doctor/<int:pk>/my_schedule/', MySchedule.as_view(), name='my_schedule'),

    path('dashboard/appointment/appoinment_list', AppointmentListsView.as_view(), name="appointment_lists"),



]