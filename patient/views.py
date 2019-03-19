from django.shortcuts import render,redirect
from user.decorators import *
from django.views.generic import *
from django.contrib import messages
from doctor.models import Doctor
from service.models import Service
from .models import *
from django.contrib.auth.decorators import login_required,permission_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User,Group
from django.utils.decorators import method_decorator
from .forms import *
from history.models import History
from appointment.models import Appointment
# Create your views here.
@method_decorator([login_required(login_url='login'),group_required('Staff')],name='dispatch')
class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    # fields = '__all__'
    def form_valid(self, form):
        # super().form_valid(form)
        f_name = self.request.POST.get('first_name')
        mobile_no= self.request.POST.get('mobile_no')
        print(f_name,mobile_no)
        username = f_name+mobile_no
        password = "password"+mobile_no
        user = User.objects.create_user(self,username=username,password=password)
        user.form.save()
        user.save()
        group = Group.objects.get(name='Patient')
        group.user_set.add(user)
        group.save()
        messages.success(self.request,'Patient is successfully Added.')
        return redirect('patient:patient_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    success_url = reverse_lazy('patient:patient_list')


@method_decorator([login_required(login_url='login'),group_required('Staff')],name='dispatch')
class PatientCreateViews(View):
    template_name='patient/patient_form.html'
    form = PatientForm()
    def get(self,request):
        context={
            'form':self.form,
        }
        return render(request,self.template_name,context)

    def post(self,request):
        form = PatientForm(request.POST)


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
            patient = form.save(commit=False)

            patient.user=user

            patient.save()

            group = Group.objects.get(name='Patient')
            group.user_set.add(user)
            group.save()
            messages.success(self.request, 'Patient is successfully Added.')
            return redirect('patient:patient_list')
        else:
            return render(request,self.template_name,{'form':form})


@method_decorator([login_required(login_url='login'),group_required('Staff')],name='dispatch')
class PatientDetailView(DetailView):

    model = Patient
    queryset = Patient.objects.all().select_related("user")
    context_object_name = 'patient'

@method_decorator([login_required(login_url='login'),group_required('Staff')],name='dispatch')
class PatientUpdateView(UpdateView):
    model = Patient
    # fields = '__all__'
    form_class = PatientForm
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        super().form_valid(form)
        form.save()
        messages.success(self.request,'Patient is successfully Added.')

    success_url = reverse_lazy('patient:patient_list')


@method_decorator([login_required(login_url='login'),group_required('Reciepnist','Staff','Accountant')],name='dispatch')
class PatientListView(ListView):
    model = Patient
    queryset = Patient.objects.all().select_related("p_district").select_related("t_district")
    context_object_name = 'patient'


def load_districts(request):
    province_id = request.GET.get('province')
    # print("province_id",province_id)
    districts = District.objects.filter(province_id=province_id).order_by('district')
    # print(districts)
    return render(request, 'patient/district_dropdown_list_options.html', {'districts': districts})



def load_municipalities(request):
    district_id = request.GET.get('district')
   # print("district_id",district_id)
    municipalities = Municipality.objects.filter(district_id=district_id).order_by('municipality')
    #print(municipalities)
    return render(request, 'patient/municipality_dropdown_list_options.html', {'municipalities':municipalities})


def load_wards(request):
    muni_id = request.GET.get('municipality')
    #print("muni_id",muni_id)
    wards = Ward.objects.filter(municipality_id=muni_id).order_by('ward_no')
   # print(wards)
    return render(request, 'patient/ward_dropdown_list_options.html', {'wards':wards})


def mydetail(reqeust,pk):
    user = User.objects.get(pk=pk)
    patient = Patient.objects.get(user=user)
    return render(reqeust,'patient/patient_detail.html',{'patient':patient})


@method_decorator([login_required(login_url='login'),group_required('Staff')],name='dispatch')
class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    # fields = ['first_name','middle_name','last_name','age','email','citizenship_number','sex','mobile_no','phone_no','p_province','p_district','p_municipality',
    #           'p_ward_no','t_province','t_district','t_municipality','t_ward_no','p_street','t_street','ethical_group']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('patient:patient_list')



def add_patient_service(request,id):
    template_name = "patient/patient_service.html"
    service = Service.objects.all()
    doctor = Doctor.objects.all()

    print('pid=',id)
    context = {
        'medicine': service,
        'doctor': doctor,
        'p_id':id,
    }

    return render(request, template_name, context)





class PatientVisitListView(ListView):
    model = PatientVisit
    context_object_name = 'patient_visit'



class PatientVisitDetailView(DetailView):
    model = PatientVisit
    context_object_name = 'patient_visit'


class PatientService(View):
    template_name="patient/patient_service.html"
    service = Service.objects.all()
    doctor = Doctor.objects.all()
    context={
        'medicine':service,
        'doctor':doctor,
    }
    def get(self,request):

        return render(request,self.template_name,self.context)
    def post(self,request):

        return render(request, self.template_name, self.context)


from django.http import JsonResponse
#validate citizenship number
def validate_citizenshipnumber(request):
    citizenship = request.GET.get('citizenship')
    # print(citizenship,"citizenship")
    data = {
        'is_taken': Patient.objects.filter(citizenship_number=citizenship).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'This citizenship number is already exists.'
    return JsonResponse(data)




# class MyAppointment(View):
#
#     template_name = "patient/patient_appointment.html"
#
#     def get(self,reqeust,pk):
#         patient = Patient.objects.get(user = pk)
#         appointment = Appointment.objects.filter(patient = patient)
#         context ={
#             'appointment': appointment,
#         }
#         return render(reqeust,self.template_name,context)



