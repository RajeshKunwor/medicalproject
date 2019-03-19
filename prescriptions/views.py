from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user.decorators import *
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.forms import formset_factory
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class PrescriptionCreateView(View):
#     template_name='prescriptions/prescription_form.html'
#     p_form = PrescriptionForm()
#
#     def get(self,request):
#         context={
#             'p_form':self.p_form,
#
#
#         }
#         return render(request,self.template_name,context)
#     def post(self,request):
#         form = PrescriptionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # id = Prescription.objects.latest('id')
#             # print("id=",id.id)
#             # return redirect("prescriptions:prescribedmedicine_create",id.id)
#             return redirect("prescriptions:prescription_list")


@method_decorator([login_required(login_url='login'),group_required('Staff','Reciepnist')],name='dispatch')
class PrescriptionListView(View):
    template_name="prescriptions/prescription_list.html"
    form = PrescriptionForm()

    def get(self,request,pk):
        prescription = Prescription.objects.filter(patient_id = pk).select_related('patient','doctor','service','observation')
        patient =Patient.objects.select_related('user').get(pk=pk)
        context={
            'patient':patient,
            'prescription':prescription,
            'form':self.form,
        }
        global status
        status=request.GET.get('value')
        return render(request, self.template_name, context)

    @method_decorator([login_required(login_url='login'), group_required('Staff')], name='dispatch')
    def post(self, request,pk):

        form = PrescriptionForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            # print(request.POST)
            instance=form.save(commit=False)

            instance.patient_id = pk
            instance.save()

            # return JsonResponse({'success': True})

            print(status)
            if status =='true':

                return redirect('prescriptions:prescribedmedicine_create',instance.pk)
            else:
                return redirect('prescriptions:prescription_list',pk)

        else:
            prescription = Prescription.objects.filter(patient_id=pk)
            patient = Patient.objects.get(pk=pk)

            context = {
                'patient': patient,
                'prescription': prescription,
                'form': self.form,


            }
            return render(request, self.template_name, context)



@method_decorator([login_required(login_url='login'), group_required('Staff')],name='dispatch')
class PrescriptionUpdateView(UpdateView):
    model = Prescription
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('prescriptions:prescription_list')

#
# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class PrescriptionListView(ListView):
#     model = Prescription
#     context_object_name = 'prescription'
#



# class PrescribedMedicineCreateView(View):
#     form = PrescribedMedicineForm()
#     template_name = 'prescriptions/prescribedmedicine.html'
#
#     def get(self, request,pk):
#         # print("Pk",pk)
#
#         context = {
#             'form': self.form,
#
#
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request,pk):
#
#         form = PrescribedMedicineForm(request.POST)
#         # print(request.POST)
#         if form.is_valid():
#             #print(request.POST)
#             instance=form.save(commit=False)
#
#             instance.prescription_id = pk
#             instance.save()
#
#             return redirect('prescriptions:prescription_list')
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

@method_decorator([login_required(login_url='login'), group_required('Staff')],name='dispatch')
class PrescribedMedicinesCreateView(View):
    extra_forms = 0
    PrescribedmedicineFormSet = formset_factory(PrescribedMedicineForm, extra=extra_forms, max_num=20, min_num=1)
    extra_forms = 1

    def get(self, request,pk):
        formset = self.PrescribedmedicineFormSet()
        return render(request, 'prescriptions/prescribedmedicine.html', {'formset': formset})

    def post(self, request,pk):
        if 'additems' in self.request.POST and self.request.POST['additems'] == 'true':
            formset_dictionary_copy = self.request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(
                formset_dictionary_copy['form-TOTAL_FORMS']) + self.extra_forms

            formset = self.PrescribedmedicineFormSet(formset_dictionary_copy)
            return render(request, 'prescriptions/prescribedmedicine.html', {'formset': formset})

        elif 'removeitems' in self.request.POST and self.request.POST['removeitems'] == 'true':
            formset_dictionary_copy = self.request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(
                formset_dictionary_copy['form-TOTAL_FORMS']) - self.extra_forms

            formset = self.PrescribedmedicineFormSet(formset_dictionary_copy)
            return render(request, 'prescriptions/prescribedmedicine.html', {'formset': formset})
        else:

            formset = self.PrescribedmedicineFormSet(request.POST)
            if formset.is_valid():
                for f in formset:
                    # print(f)
                    instance = f.save(commit=False)

                    instance.prescription_id = pk
                    instance.save()

                return redirect('prescriptions:prescription_list',instance.prescription.patient.pk)

        formset = self.PrescribedmedicineFormSet()

        return render(request, 'prescriptions/prescribedmedicine.html', {'formset': formset})



@method_decorator([login_required(login_url='login'), group_required('Staff')],name='dispatch')
class PrescribedMedicineListView(ListView):

    template_name="prescriptions/prescribedmedicine_list.html"

    def get(self,request,pk):
        prescription = Prescription.objects.get(pk = pk)
        precribedmedicine = PrescribedMedicine.objects.filter(prescription_id=pk)
        context={
            'prescription':prescription,
            'prescribedmedicine':precribedmedicine,
        }

        return render(request,"prescriptions/prescribedmedicine_list.html",context)



def load_observation(request):
    patient_id = request.GET.get('patient')
    # print("doctor_id",doctor_id)
    observation = Observation.objects.filter(
        Q(patient_id=patient_id))

    # print(schedule)
    return render(request, 'prescriptions/observation_dropdown_list_options.html', {'observation': observation})



