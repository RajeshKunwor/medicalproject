from django.urls import path
from .views import *
urlpatterns =[
    path('dashboard/<int:pk>/observation_create/',ObservationCreateView.as_view(),name='observation_create'),
    path('dashboard/<int:pk>/observation_list/',ObservationListView.as_view(),name='observation_list'),
    path('dashboard/<int:pk>/observation_update',ObservationUpdateView.as_view(),name='observation_update'),

]