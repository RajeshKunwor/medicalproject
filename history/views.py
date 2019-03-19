from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import History
from user.decorators import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from .forms import HistoryForm
from patient.models import Patient
from django.http import  JsonResponse
# Create your views here.
@method_decorator([login_required(login_url='login'), group_required('Staff')],name='dispatch')
class HistoryCreateView(View):
    form = HistoryForm()
    template_name = 'history/history_form.html'

    def get(self, request,pk):
        # print("Pk",pk)
        patient = Patient.objects.get(pk=pk)
        context = {
            'form': self.form,
            'patient':patient,


        }
        return render(request, self.template_name, context)

    def post(self, request,pk):

        form = HistoryForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            print(request.POST)
            instance=form.save(commit=False)

            instance.patient_id = pk
            instance.save()

            #return JsonResponse({'success': True})


            return redirect('history:history_list',pk)

        else:

            context = {
                'form': self.form,


            }
            return render(request, self.template_name, context)





@method_decorator([login_required(login_url='login'), group_required('Staff')],name='dispatch')
class HistoryUpdateView(UpdateView):
    model = History
    form_class = HistoryForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('patient:patient_list')


@method_decorator([login_required(login_url='login'), group_required('Staff','Reciepnist')],name='dispatch')
class HistoryListView(View):
    template_name="history/history_list.html"
    form = HistoryForm()
    def get(self,request,pk):
        history = History.objects.filter(patient_id = pk)
        patient = Patient.objects.select_related('user').get(pk=pk)
        context={
            'patient':patient,
            'history':history,
            'form':self.form,
        }
        return render(request, self.template_name, context)

    @method_decorator([login_required(login_url='login'), group_required('Staff')], name='dispatch')
    def post(self, request,pk):

        form = HistoryForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            # print(request.POST)
            instance=form.save(commit=False)

            instance.patient_id = pk
            instance.save()

            # return JsonResponse({'success': True})


            return redirect('history:history_list',pk)

        else:

            context = {
                'form': self.form,


            }
            return render(request, self.template_name, context)


@method_decorator([login_required(login_url='login'), group_required('Patient')],name='dispatch')
class MyHistoryList(View):

    template_name = "history/patient_history.html"

    def get(self,request,pk):
        patient = Patient.objects.select_related("user").get(user = pk)
        history = History.objects.filter(patient = patient).select_related("patient")
        print(history)
        context = {
            'history': history,
        }
        return render(request,self.template_name,context)
