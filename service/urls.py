from django.urls import path
from .views import *
urlpatterns =[

    path('dashboard/service_create/',ServiceCreateView.as_view(),name='service_create'),
    path('dashboard/service_list/',ServiceListView.as_view(),name='service_list'),
    path('dashboard/<int:pk>/service_update/',ServiceUpdateView.as_view(),name='service_update'),
    path('dashboard/<int:pk>/service_delete/',ServiceDeleteView.as_view(),name = 'service_delete')



]