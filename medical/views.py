from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.contrib.auth.decorators import login_required,permission_required
from django.urls import reverse_lazy
from .decorators import *
from django.utils.decorators import method_decorator
from .forms import *
# Create your views here.

# @login_required(login_url='login')
# def dashboard(request):
#     male_count = Patient.objects.filter(sex='Male').count()
#     female_count = Patient.objects.filter(sex ='Female').count()
#     child_count = Patient.objects.filter(age__lt= 17).count()
#     context = {
#         'male_count':male_count,
#         'female_count':female_count,
#         'child_count':child_count,
#     }
#     return render(request,"base.html",context)

# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class ProvinceCreateView(CreateView):
#     model = Province
#     fields = '__all__'
#     success_url = reverse_lazy('province_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class ProvinceUpdateView(UpdateView):
#     model = Province
#     fields = '__all__'
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('province_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class ProvinceListView(ListView):
#     model = Province
#     context_object_name = 'province'
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class DistrictCreateView(CreateView):
#     model = District
#     fields = '__all__'
#     success_url = reverse_lazy('district_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class DistrictUpdateView(UpdateView):
#     model = District
#     fields = '__all__'
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('district_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class DistrictListView(ListView):
#     model = District
#     context_object_name = 'district'
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class MunicipalityCreateView(CreateView):
#     model = Municipality
#     fields = '__all__'
#     success_url = reverse_lazy('municipality_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class MunicipalityUpdateView(UpdateView):
#     model = Municipality
#     fields = '__all__'
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('municipality_list')
#
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class MunicipalityListView(ListView):
#     model = Municipality
#     context_object_name = 'municipality'
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class WardCreateView(CreateView):
#     model = Ward
#     fields = '__all__'
#     success_url = reverse_lazy('ward_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class WardUpdateView(UpdateView):
#     model = Ward
#     fields = '__all__'
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('ward_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class WardListView(ListView):
#     model = Ward
#     context_object_name = 'ward'
#
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class MedicineCreateView(CreateView):
#     model = Medicine
#     fields = '__all__'
#     success_url = reverse_lazy('medicine_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class MedicineUpdateView(UpdateView):
#     model = Medicine
#     fields = '__all__'
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('medicine_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class MedicineListView(ListView):
#     model = Medicine
#     context_object_name = 'medicine'
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class ServiceTypeCreateView(CreateView):
#     model = ServiceType
#     fields = '__all__'
#     success_url = reverse_lazy('servicetype_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class ServiceTypeUpdateView(UpdateView):
#     model = ServiceType
#     fields = '__all__'
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('servicetype_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class ServiceTypeListView(ListView):
#     model = ServiceType
#     context_object_name = 'servicetype'
#
#
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class DoctorCreateView(CreateView):
#     model = Doctor
#     #form_class = PatientForm
#     fields = '__all__'
#     success_url = reverse_lazy('doctor_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class DoctorUpdateView(UpdateView):
#     model = Doctor
#     fields = '__all__'
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('doctor_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class DoctorListView(ListView):
#     model = Doctor
#     context_object_name = 'doctor'
#
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class DoctorScheduleCreateView(CreateView):
#     model = DoctorSchedule
#     #form_class = PatientForm
#     fields = '__all__'
#     success_url = reverse_lazy('doctor_schedule_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class DoctorScheduleUpdateView(UpdateView):
#     model = DoctorSchedule
#     fields = '__all__'
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('doctor_schedule_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class DoctorScheduleListView(ListView):
#     model = DoctorSchedule
#     context_object_name = 'doctor_schedule'
#
#
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class PatientCreateView(CreateView):
#     model = Patient
#     form_class = PatientForm
#     #fields = '__all__'
#     success_url = reverse_lazy('patient_list')
#
#
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class PatientUpdateView(UpdateView):
#     model = Patient
#     fields = '__all__'
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('patient_list')
#
#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class PatientListView(ListView):
#     model = Patient
#     context_object_name = 'patient'
#
#
# def load_districts(request):
#     province_id = request.GET.get('province')
#     #print("province_id",province_id)
#     districts = District.objects.filter(provice_id=province_id).order_by('district')
#     #print(districts)
#     return render(request, 'medical/district_dropdown_list_options.html', {'districts': districts})
#
#
#
# def load_municipalities(request):
#     district_id = request.GET.get('district')
#    # print("district_id",district_id)
#     municipalities = Municipality.objects.filter(district_id=district_id).order_by('municipality')
#     #print(municipalities)
#     return render(request, 'medical/municipality_dropdown_list_options.html', {'municipalities':municipalities})
#
#
# def load_wards(request):
#     muni_id = request.GET.get('municipality')
#     #print("muni_id",muni_id)
#     wards = Ward.objects.filter(municipality_id=muni_id).order_by('ward_no')
#    # print(wards)
#     return render(request, 'medical/ward_dropdown_list_options.html', {'wards':wards})
#
#
# class PersonCreateView(CreateView):
#     model = Person
#     form_class = PersonForm
#     success_url = reverse_lazy('')