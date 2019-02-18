from django.urls import path
from .views import *
urlpatterns =[
    path('dashboard/<int:pk>/history_create/',HistoryCreateView.as_view(),name='history_create'),
    path('dashboard/<int:pk>/history_list/',HistoryListView.as_view(),name='history_list'),
    path('dashboard/<int:pk>/history_update',HistoryUpdateView.as_view(),name='history_update'),

]