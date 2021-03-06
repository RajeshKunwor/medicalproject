from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user.decorators import *
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User,Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from prescriptions.models import Prescription
from patient.models import Patient
from home.models import Notification
import datetime
# Create your views here.
@method_decorator([login_required(login_url='login'),group_required('Staff')],name='dispatch')
class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    # fields = '__all__'

    def form_valid(self, form):
        super().form_valid(form)
        form.save()

        messages.success(self.request,'Doctor is successfully Added.')
        return redirect('doctor:doctor_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    success_url = reverse_lazy('doctor:doctor_list')


@method_decorator([login_required(login_url='login'), group_required('Staff')],name='dispatch')
class DoctorCreateViews(View):
    template_name = 'doctor/doctor_form.html'
    form = DoctorForm()

    def get(self, request):
        context = {
            'form': self.form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = DoctorForm(request.POST)

        if form.is_valid():
            # user.save()
            f_name = form.cleaned_data['first_name']
            mobile_no = form.cleaned_data['mobile_no']
            # print(f_name, mobile_no)

            username = f_name + mobile_no
            password = "password" + mobile_no
            user = User.objects.create_user(username=username, password=password)
            # print("user is", user.id)
            #
            # print("user is",user)
            doctor = form.save(commit=False)

            doctor.user = user

            doctor.save()

            group = Group.objects.get(name='Doctor')
            group.user_set.add(user)
            group.save()
            messages.success(self.request, 'Doctor is successfully Added.')
            return redirect('doctor:doctor_list')
        else:
            return render(request, self.template_name, {'form': form})

@method_decorator([login_required(login_url='login'),group_required('Staff')],name='dispatch')
class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    # fields = ['first_name','middle_name','last_name','age','citizenship_number','sex','year_of_birth','mobile_no','phone_no','p_province','p_district','p_municipality',
    #           'p_ward_no','t_province','t_district','t_municipality','t_ward_no','p_street','t_street','specialist','ethical_group']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('doctor:doctor_list')


@method_decorator([login_required(login_url='login'),group_required('Staff','Reciepnist')],name='dispatch')
class DoctorListView(ListView):
    model = Doctor
    paginate_by = 5
    context_object_name = 'doctor'


class DoctorDetailView(DetailView):
    model = Doctor


def mydetail(reqeust,pk):
    user = User.objects.get(pk=pk)
    doctor = Doctor.objects.get(user=user)
    return render(reqeust,'doctor/doctor_detail.html',{'doctor':doctor})


def load_districts(request):
    province_id = request.GET.get('province')
    #print("province_id",province_id)
    districts = District.objects.filter(province_id=province_id).order_by('district')
    #print(districts)
    return render(request, 'doctor/district_dropdown_list_options.html', {'districts': districts})



def load_municipalities(request):
    district_id = request.GET.get('district')
   # print("district_id",district_id)
    municipalities = Municipality.objects.filter(district_id=district_id).order_by('municipality')
    #print(municipalities)
    return render(request, 'doctor/municipality_dropdown_list_options.html', {'municipalities':municipalities})


def load_wards(request):
    muni_id = request.GET.get('municipality')
    #print("muni_id",muni_id)
    wards = Ward.objects.filter(municipality_id=muni_id).order_by('ward_no')
   # print(wards)
    return render(request, 'doctor/ward_dropdown_list_options.html', {'wards':wards})



from django.http import JsonResponse
#validate citizenship number
def validate_citizenshipnumber(request):
    citizenship = request.GET.get('citizenship')
    # print(citizenship,"citizenship")
    data = {
        'is_taken': Doctor.objects.filter(citizenship_number=citizenship).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'This citizenship number is already exists.'
    return JsonResponse(data)










# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class DoctorScheduleCreateView(View):
#     form = DoctorScheduleForm()
#     template_name = 'doctor/doctorschedule_form.html'
#
#     def get(self, request,pk):
#         # print("Pk",pk)
#         doctor = Doctor.objects.get(pk=pk)
#         context = {
#             'form': self.form,
#             'doctor':doctor,
#
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request,pk):
#
#         form = DoctorScheduleForm(request.POST)
#         # print(request.POST)
#         if form.is_valid():
#             print(request.POST)
#             instance=form.save(commit=False)
#
#             instance.doctor_id = pk
#             instance.save()
#
#             return redirect('doctor:doctor_list')
#
#         else:
#
#             context = {
#                 'form': self.form,
#
#
#             }
#             return render(request, self.template_name, context)
#
#
#


@method_decorator([login_required(login_url='login'),group_required('Staff')],name='dispatch')
class DoctorScheduleUpdateView(UpdateView):
    model = DoctorSchedule
    form_class = DoctorScheduleForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('doctor:doctor_schedule_list')


@method_decorator([login_required(login_url='login'),group_required('Staff','Reciepnist')],name='dispatch')
class DoctorScheduleListView(View):
    template_name="doctor/doctorschedule_list.html"
    form = DoctorScheduleForm()

    def get(self,request,pk):

        doctor_schedule = DoctorSchedule.objects.filter(doctor_id = pk)
        doctor = Doctor.objects.get(pk=pk)
        page = request.GET.get('page', 1)

        paginator = Paginator(doctor_schedule, 5)
        try:
           doctor_schedule = paginator.page(page)
        except PageNotAnInteger:
            doctor_schedule = paginator.page(1)
        except EmptyPage:
            doctor_schedule = paginator.page(paginator.num_pages)
        context={
            'doctor':doctor,
            'doctor_schedule':doctor_schedule,
            'form':self.form,
        }

        return render(request,self.template_name,context)

    @method_decorator([login_required(login_url='login'), group_required('Staff')], name='dispatch')
    def post(self, request,pk):

        form = DoctorScheduleForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            print(request.POST)
            instance=form.save(commit=False)

            instance.doctor_id = pk
            instance.save()
            sender_user = request.user
            receiver_user = instance.doctor.user
            message = f"Your schedule at { instance.date } has been created."
            date = datetime.date.today()
            time = datetime.datetime.now().time()
            notification = Notification(sender_user=sender_user, message=message, status=False,
                                        receiver_user=receiver_user, date=date, time=time)
            notification.save()
            messages.success(request,"Schedule is successfully Created.")
            return redirect('doctor:doctor_schedule_list',pk)

        else:

            context = {
                'form': self.form,


            }
            return render(request, self.template_name, context)


@method_decorator([login_required(login_url='login'), group_required('Doctor')],name='dispatch')
class MyPatient(View):

    template_name ="doctor/my_patient.html"
    def get(self,request,pk):

        doctor = Doctor.objects.get(user=pk)
        patient = Prescription.objects.filter(doctor=doctor).select_related('patient','doctor')
        patients = []
        for p in patient:
            patients.append(p.patient.id)

        # print(patients)

        pat = []
        for p in patients:
            if p not in pat:
                pat.append(p)
        # print(pat)
        patient = Patient.objects.filter(id__in=pat)

        context = {
            'patient': patient,
        }

        return render(request, self.template_name, context)

