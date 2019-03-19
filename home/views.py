from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.contrib.auth.decorators import login_required,permission_required
from django.urls import reverse_lazy
from user.decorators import *
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from patient.models import Patient
from doctor.models import Doctor,DoctorSchedule
from observation.models import Observation
import datetime
from appointment.models import Appointment
from django.db.models import Q

from django.http import JsonResponse

# Create your views here.


def hasGroup(user, groupName):
    group = Group.objects.get(name=groupName)
    return True if group in user.groups.all() else False


@login_required(login_url='login')
def dashboard(request):
    # male_count = Patient.objects.filter(sex='Male').count()
    patient = Patient.objects.all().select_related('user').count()
    # female_count = Patient.objects.filter(sex ='Female').count()
    # child_count = Patient.objects.filter(age__lt= 17).count()
    doctor = Doctor.objects.all().select_related('user').count()
    doctor_schedule = DoctorSchedule.objects.filter(date=datetime.date.today()).select_related("doctor")

    regular_patient = Observation.objects.all()
    id=[]
    appointment = Appointment.objects.all().select_related('appointment_schedule')
    patient_appointment = None
    for pa in appointment:
        date = pa.appointment_schedule.date
        if date == datetime.date.today():

            id.append(pa.id)
            patient_appointment = Appointment.objects.filter(pk__in = id).select_related("patient").select_related("doctor")

    appointment = Appointment.objects.filter(status='request').select_related('patient','doctor','appointment_schedule')
    count = appointment.count()

    notification = Notification.objects.filter(Q(status=False)&Q(receiver_user=request.user))
    notification_count = notification.count()

    # print(patient_appointment)

    # print(regular_patient)
    # print(list(regular_patient))
    # print(doctor_schedule)
    context = {
            # 'male_count':male_count,
            # 'female_count':female_count,
            # 'child_count':child_count,
            'count': count,
            'doctor': doctor,
            'patient': patient,
            'doctor_schedule': doctor_schedule,
            'patient_appointment': patient_appointment,
            'regular_patient': regular_patient,
            'notification': notification,
            'notification_count': notification_count,

    }
    # import pdb
    # pdb.set_trace()

    if hasGroup(request.user,'Patient'):

        return render(request,'patient/patientdashboard.html', context)

    elif hasGroup(request.user,'Doctor'):
        return render(request,'doctor/doctordashboard.html',context)

    return render(request,"home/dashboard.html",context)


def view_notification(request):
    pk = request.GET.get('notification_id')
    print("notification id", pk)
    notification = Notification.objects.get(id=pk)
    notification.status = True
    notification.save()
    print("status", notification.status)
    data ={}
    data['msg'] = "success"
    return JsonResponse(data)