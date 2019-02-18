"""medicalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test


urlpatterns = [
    path('admin/', admin.site.urls),
    url('home/',include(('home.urls','home'),namespace='home')),
    url('medical/',include(('medical.urls','medical'),namespace="medical")),
    url('location/',include(('location.urls','location'),namespace="location")),
    url('doctor/',include(('doctor.urls','doctor'),namespace="doctor")),
    path('patient/',include(('patient.urls','patient'),namespace="patient")),
    path('user/',include(('user.urls','user'),namespace="user")),
    path('medicine/',include(('medicine.urls',',medicine'),namespace="medicine")),
    path('appointment/',include(('appointment.urls','appointment'),namespace="appointment")),
    path('prescriptions/',include(('prescriptions.urls','prescriptions'),namespace='prescriptions')),
    path('service/',include(('service.urls','service'),namespace='service')),
    path('history/',include(('history.urls','history'),namespace='history')),
    path('observation/',include(('observation.urls','observation'),namespace='observation')),
    path('dashboard/change_password',login_required(login_url='login')(PasswordChangeView.as_view(template_name='registration/change_password.html')),name='change_password'),
    path('dashboard/password_change_done',login_required(login_url='login')(PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html')),name ='password_change_done'),
    path('',LoginView.as_view(template_name='registration/login.html',redirect_authenticated_user = True),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
]
