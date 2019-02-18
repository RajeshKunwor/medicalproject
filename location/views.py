from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.contrib.auth.decorators import login_required,permission_required
from django.urls import reverse_lazy
from user.decorators import *
from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class ProvinceCreateView(CreateView):
    model = Province
    fields = '__all__'
    success_url = reverse_lazy('location:province_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class ProvinceUpdateView(UpdateView):
    model = Province
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('location:province_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class ProvinceListView(ListView):
    model = Province
    context_object_name = 'province'


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class DistrictCreateView(CreateView):
    model = District
    fields = '__all__'
    success_url = reverse_lazy('location:district_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class DistrictUpdateView(UpdateView):
    model = District
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('location:district_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class DistrictListView(ListView):
    model = District
    context_object_name = 'district'


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class MunicipalityCreateView(CreateView):
    model = Municipality
    fields = '__all__'
    success_url = reverse_lazy('location:municipality_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class MunicipalityUpdateView(UpdateView):
    model = Municipality
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('location:municipality_list')



@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class MunicipalityListView(ListView):
    model = Municipality
    context_object_name = 'municipality'


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class WardCreateView(CreateView):
    model = Ward
    fields = '__all__'
    success_url = reverse_lazy('location:ward_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class WardUpdateView(UpdateView):
    model = Ward
    fields = ['ward_no']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('location:ward_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class WardListView(ListView):
    model = Ward
    context_object_name = 'ward'


