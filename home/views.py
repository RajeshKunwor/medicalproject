from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.contrib.auth.decorators import login_required,permission_required
from django.urls import reverse_lazy
from user.decorators import *
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
# Create your views here.


def hasGroup(user, groupName):
    group = Group.objects.get(name=groupName)
    return True if group in user.groups.all() else False


@login_required(login_url='login')
def dashboard(request):

    if hasGroup(request.user,'Patient'):
        return render(request,'patient/patientdashboard.html')

    elif hasGroup(request.user,'Doctor'):
        return render(request,'doctor/doctordashboard.html')

    return render(request,"base.html")