from django.urls import path
from .views import *
urlpatterns =[

    path('dashboard/province_create/',ProvinceCreateView.as_view(),name='province_create'),
    path('dashboard/province_list/',ProvinceListView.as_view(),name='province_list'),
    path('dashbaord/<int:pk>/province_update',ProvinceUpdateView.as_view(),name='province_update'),

    path('dashboard/district_create/',DistrictCreateView.as_view(),name='district_create'),
    path('dashboard/district_list/',DistrictListView.as_view(),name='district_list'),
    path('dashbaord/<int:pk>/district_update',DistrictUpdateView.as_view(),name='district_update'),

    path('dashboard/municipality_create/',MunicipalityCreateView.as_view(),name='municipality_create'),
    path('dashboard/municipality_list/',MunicipalityListView.as_view(),name='municipality_list'),
    path('dashbaord/<int:pk>/municipality_update',MunicipalityUpdateView.as_view(),name='municipality_update'),

    path('dashboard/ward_create/',WardCreateView.as_view(),name='ward_create'),
    path('dashboard/ward_list/',WardListView.as_view(),name='ward_list'),
    path('dashbaord/<int:pk>/ward_update',WardUpdateView.as_view(),name='ward_update'),

]