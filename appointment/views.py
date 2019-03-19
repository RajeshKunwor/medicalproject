from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user.decorators import *
from django.views.generic import *
from django.db.models import Q
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.http import JsonResponse
import datetime
from django.contrib import messages
from home.models import Notification
from django.contrib.auth.models import Group,User
# Create your views here.
@method_decorator([login_required(login_url='login'),group_required('Staff','Reciepnist')],name='dispatch')
class AppointmentCreateView(CreateView):
    model = Appointment
    #form_class = PatientForm
    fields = '__all__'
    success_url = reverse_lazy('appointment_list')


@method_decorator([login_required(login_url='login'),group_required('Staff','Reciepnist')],name='dispatch')
class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('appointment_list')


def load_schedule(request):
    doctor_id = request.GET.get('doctor')
    # print("doctor_id",doctor_id)
    schedule = DoctorSchedule.objects.filter(Q(doctor_id=doctor_id,date=datetime.date.today())|Q(doctor_id=doctor_id,date__gt=datetime.date.today()))


    # print(schedule)
    return render(request, 'appointment/schedule_dropdown_list_options.html', {'schedule': schedule})

@method_decorator([login_required(login_url='login'), group_required('Staff','Reciepnist')], name='dispatch')
class AppointmentListsView(ListView):

    model = Appointment
    queryset = Appointment.objects.all().order_by('-pk').select_related('patient','appointment_schedule')
    template_name_suffix = '_lists'
    paginate_by = 10
    context_object_name = 'appointment'

@method_decorator([login_required(login_url='login'), group_required('Staff','Reciepnist')],name='dispatch')
class AppointmentListView(View):
    template_name="appointment/appointment_list.html"
    form = AppointmentForm()
    def get(self,request,pk):
        appointment = Appointment.objects.filter(patient_id = pk).select_related('doctor','patient','appointment_schedule')
        patient =Patient.objects.select_related('user').get(pk=pk)
        context={
            'patient':patient,
            'appointment':appointment,
            'form':self.form,
        }
        return render(request, self.template_name, context)

    def post(self, request,pk):

        form = AppointmentForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            print(request.POST)
            instance = form.save(commit=False)

            instance.patient_id = pk
            instance.status = 'confirm'

            instance.save()
            sender_user = request.user
            receiver_user = instance.doctor.user
            message = f"Your appointment for { instance.patient} at { instance.appointment_schedule } has been created."
            date = datetime.date.today()
            time = datetime.datetime.now().time()
            notification = Notification(sender_user=sender_user, message=message, status=False,
                                        receiver_user=receiver_user, date=date, time=time)
            notification.save()
            print(notification)


            # return JsonResponse({'success': True})

            return redirect('appointment:appointment_list', pk)

        else:

            context = {
                'form': self.form,


            }
            return render(request, self.template_name, context)


@method_decorator([login_required(login_url='login'),group_required('Patient')],name='dispatch')
class MyAppointment(View):

    template_name = "appointment/patient_appointment.html"

    def get(self,reqeust,pk):
        patient = Patient.objects.get(user = pk)
        appointment = Appointment.objects.filter(patient = patient).select_related('patient','doctor','appointment_schedule')
        context ={
            'appointment': appointment,
        }
        return render(reqeust,self.template_name,context)


@method_decorator([login_required(login_url='login'),group_required('Doctor')],name='dispatch')
class MySchedule(View):

    template_name = "appointment/doctor_schedule.html"

    def get(self,reqeust,pk):
        doctor = Doctor.objects.select_related('user').get(user = pk)
        doctor_schedule = DoctorSchedule.objects.filter(doctor=doctor).select_related('doctor').order_by('-date')
        print(doctor_schedule)
        context ={
            'doctor_schedule': doctor_schedule,
        }
        return render(reqeust,self.template_name,context)


@method_decorator([login_required(login_url='login'),group_required('Patient')],name='dispatch')
class RequestAppointment(View):

    template = 'appointment/request_appointment.html'
    form = AppointmentForm()
    def get(self,request,pk):

        context ={
            'form': self.form,
        }
        return render(request, self.template, context)


    def post(self,request,pk):

        form = AppointmentForm(request.POST)
        # print(request.POST)
        if form.is_valid():

            instance = form.save(commit=False)
            patient_id = Patient.objects.get(user=pk)
            instance.patient_id = patient_id.id
            instance.status = 'request'


            # sender_user = request.user
            #
            # receiver_user =
            # message = f"Your appointment for { instance.doctor } at { instance.appointment_schedule } has been confirmed."
            # date = datetime.date.today()
            # time = datetime.datetime.now().time()
            # notification = Notification(sender_user=sender_user, message=message, status=False,
            #                             receiver_user=receiver_user, date=date, time=time)
            # notification.save()


            instance.save()

            # return JsonResponse({'success': True})
            messages.success(self.request, 'Request is successfully sent.')
            return redirect('home:dashboard')

        else:

            context = {
                'form': self.form,

            }
            return render(request, self.template_name, context)


class NewAppointment(View):

    template_name = "appointment/new_appointment.html"

    def get(self, request):

        appointment = Appointment.objects.filter(status='request').select_related('patient','doctor','appointment_schedule')
        count = appointment.count()
        print(count)
        context = {
            'newappointment': appointment,


        }
        return render(request, self.template_name,context)

    def post(self,request):

        pass


def confirm_appointment(request,pk):

    appointment = Appointment.objects.get(pk=pk)
    appointment.status = "confirm"
    sender_user = request.user
    receiver_user = appointment.patient.user
    message = f"Your appointment for { appointment.doctor } at { appointment.appointment_schedule } has been confirmed."
    date = datetime.date.today()
    time = datetime.datetime.now().time()
    notification = Notification(sender_user=sender_user, message=message, status=False,
                                receiver_user=receiver_user, date=date, time=time)
    notification.save()

    appointment.save()
    messages.success(request,"This appointment is successfully confirmed.")
    return redirect("appointment:new_appointment")


def reject_appointment(request,pk):

    appointment = Appointment.objects.get(pk=pk)
    appointment.status = "reject"
    sender_user = request.user
    receiver_user = appointment.patient.user
    message = f"Your appointment for { appointment.doctor } at { appointment.appointment_schedule } has been rejected."
    date = datetime.date.today()
    time = datetime.datetime.now().time()
    notification = Notification(sender_user=sender_user, message=message, status=False,
                                receiver_user=receiver_user, date=date, time=time)
    notification.save()

    appointment.save()
    messages.success(request,"This appointment is successfully rejected.")
    return redirect("appointment:new_appointment")


#validate citizenship number
def check_appointment(request):
    patient_id = request.GET.get('patient')
    doctor_id = request.GET.get('doctor')
    appointment_schedule_id=request.GET.get('appointment')
    #
    # print(patient_id,doctor_id,appointment_schedule_id)
    data = {
        'is_taken': Appointment.objects.filter(Q(patient_id=patient_id)& Q(doctor_id=doctor_id) & Q(appointment_schedule_id=appointment_schedule_id)).exists()
    }
    # print(data)
    if data['is_taken']:
        data['error_message'] = 'This patient is already appointed.'
    return JsonResponse(data)


def check_max_patient(request):
    doctor_id = request.GET.get('doctor')
    appointment_id = request.GET.get('appointment')
    count_appointment = Appointment.objects.filter(Q(doctor_id=doctor_id)&Q(appointment_schedule_id=appointment_id)).count()
    # print("Count is ", count_appointment)
    max_patient = DoctorSchedule.objects.get(Q(pk=appointment_id))
    # print("max_patient", max_patient.max_patient)

    if count_appointment == max_patient.max_patient:
        data={
            'is_taken': True
        }
    else:
        data = {
            'is_taken': False,
        }
    if data['is_taken']:
        data['error_message']= 'There is no appointment available.'
    return JsonResponse(data)
