from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user.decorators import *
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
# Create your views here.
@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class AppointmentCreateView(CreateView):
    model = Appointment
    #form_class = PatientForm
    fields = '__all__'
    success_url = reverse_lazy('appointment_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('appointment_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class AppointmentListView(ListView):
    model = Appointment
    context_object_name = 'appointment'


