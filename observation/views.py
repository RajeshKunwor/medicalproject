from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Observation
from user.decorators import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from .forms import ObservationForm
from patient.models import Patient
# Create your views here.
@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class ObservationCreateView(View):
    form = ObservationForm()
    template_name = 'observation/observation_form.html'

    def get(self, request,pk):
        # print("Pk",pk)
        patient = Patient.objects.select_related('user').get(pk=pk)
        context = {
            'form': self.form,
            'patient':patient,


        }
        return render(request, self.template_name, context)

    def post(self, request,pk):

        form = ObservationForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            print(request.POST)
            instance=form.save(commit=False)

            instance.patient_id = pk
            instance.save()

            return redirect('patient:patient_list')

        else:

            context = {
                'form': self.form,


            }
            return render(request, self.template_name, context)





@method_decorator([login_required(login_url='login'), group_required('Staff')],name='dispatch')
class ObservationUpdateView(UpdateView):
    model = Observation
    form_class = ObservationForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('patient:patient_list')


@method_decorator([login_required(login_url='login'), group_required('Staff','Reciepnist')],name='dispatch')
class ObservationListView(View):
    template_name = "observation/observation_list.html"
    form = ObservationForm()
    def get(self,request,pk):
        observation = Observation.objects.filter(patient_id = pk)
        patient = Patient.objects.select_related('user').get(pk=pk)
        context={
            'patient':patient,
            'observation':observation,
            'form':self.form,
        }

        return render(request,self.template_name,context)

    @method_decorator([login_required(login_url='login'), group_required('Staff')], name='dispatch')
    def post(self, request,pk):

        form = ObservationForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            print(request.POST)
            instance=form.save(commit=False)

            instance.patient_id = pk
            instance.save()

            return redirect('observation:observation_list',pk)

        else:

            context = {
                
                'form': self.form,


            }
            return render(request, self.template_name, context)
