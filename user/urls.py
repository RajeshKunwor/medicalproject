from django.urls import path
from .views import *
from . import views
urlpatterns =[



    path('dashboard/create_user/',UserCreationView.as_view(),name="create_user"),
    path('dashboard/user_list/',UserView.as_view(),name='user_list'),
    path('dashbaord/<int:pk>/update_user', UserUpdateView.as_view(), name='update_user'),
    path('dashboard/<int:pk>/delete_user', UserDeleteView.as_view(), name='delete_user'),

    path('dashboard/group_list/',GroupView.as_view(),name='group_list'),
    path('dashboard/create_group/',GroupCreationView.as_view(),name="create_group"),
    path('dashbaord/<int:pk>/delete_group',GroupDeleteView.as_view(),name='delete_group'),
    path('dashbaord/<int:pk>/update_group', GroupUpdateView.as_view(), name='update_group'),

    path("dashboard/add_user_group/",views.add_user_group,name='add-user-group'),
    path('dashboard/add_user_to_group',views.add_user_to_group,name='add_user_to_group'),

    path("dashboard/add_perm_group/",views.add_permission_group,name='add_perm_group'),
    #path("dashboard/user_group_list",views),
    path('dashboard/add_perm_to_group',views.add_permission_to_group,name='add_perm_to_group'),



]