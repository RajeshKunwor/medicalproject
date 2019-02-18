from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user.decorators import *
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
# Create your views here.
@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class ServiceCreateView(CreateView):
    model = Service
    #form_class = PatientForm
    fields = '__all__'
    success_url = reverse_lazy('service:service_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class ServiceUpdateView(UpdateView):
    model = Service
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('service:service_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class ServiceListView(ListView):
    model = Service
    context_object_name = 'service'


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class ServiceDeleteView(DeleteView):
    model = Service
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('service:service_list')