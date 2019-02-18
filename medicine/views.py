from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user.decorators import *
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
# Create your views here.
@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class MedicineCreateView(CreateView):
    model = Medicine
    #form_class = PatientForm
    fields = '__all__'
    success_url = reverse_lazy('medicine:medicine_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class MedicineUpdateView(UpdateView):
    model = Medicine
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('medicine:medicine_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class MedicineListView(ListView):
    model = Medicine
    context_object_name = 'medicine'