from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse_lazy
from .models import Bill
from user.decorators import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from .forms import BillForm
from patient.models import Patient
from prescriptions.models import *
from django.db.models import Q
from django.http import JsonResponse

# from django.template.loader import render_to_string
#
# from weasyprint import HTML
# Create your views here.
@method_decorator([login_required(login_url='login'),group_required('Accountant','Staff')],name='dispatch')
class BillCreateView(View):
    template_name="bill/bill_form"
    form = BillForm()

    def get(self,request,pk):
        bill = Bill.objects.filter(patient_id = pk)
        patient =Patient.objects.select_related('user').get(pk=pk)
        context={
            'patient': patient,
            'bill': bill,
            'form': self.form,
        }
        return render(request, self.template_name, context)

    def post(self, request,pk):

        form = BillForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            # print(request.POST)
            instance=form.save(commit=False)

            instance.patient_id = pk
            instance.save()

            # return JsonResponse({'success': True})


            return redirect('bill:bill_list',pk)

        else:

            context = {
                'form': self.form,


            }
            return render(request, self.template_name, context)



# class BillGenerateView(View):
#     def get(self,request,pk):


# @method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
# class HistoryUpdateView(UpdateView):
#     model = History
#     form_class = HistoryForm
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('patient:patient_list')


@method_decorator([login_required(login_url='login'),group_required('Staff','Reciepnist','Accountant')],name='dispatch')
class BillListView(View):
    template_name="bill/bill_list.html"
    form = BillForm()
    def get(self,request,pk):
        bill = Bill.objects.filter(patient_id = pk)
        global patient
        patient =Patient.objects.select_related('user').get(pk=pk)
        context={
            'patient':patient,
            'bill':bill,
            'form':self.form,
        }
        return render(request, self.template_name, context)

    def post(self, request,pk):

        form = BillForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            # print(request.POST)
            instance=form.save(commit=False)

            instance.patient_id = pk
            instance.save()

            # return JsonResponse({'success': True})


            return redirect('bill:generate_bill')

        else:

            context = {
                'form': self.form,


            }
            return render(request, self.template_name, context)



def load_prescription(request):
    patient_id = request.GET.get('patient')
    # print("doctor_id",doctor_id)
    prescription = Prescription.objects.filter(
        Q(patient_id=patient_id))


    # print(schedule)
    return render(request, 'bill/prescription_dropdown_list_options.html', {'prescription': prescription})





def load_service(request):
    prescription_id = request.GET.get('prescription')
    print("Prescription_id ", prescription_id)
    service = Prescription.objects.filter(
        Q(pk=prescription_id))
    prescribedmedicine = PrescribedMedicine.objects.filter(Q(prescription_id = prescription_id))
    medicine_cost =0.0

    for pm in prescribedmedicine:
        medicine_cost += pm.medicine.price*pm.quantity
    for s in service:
        service_cost = s.service.cost

    total_cost = service_cost+medicine_cost
    global context
    context = {
        'service': service,
        'prescribedmedicine': prescribedmedicine,
        'patient': patient,
        'prescription': prescription_id,
        'medicine_cost':medicine_cost,
        'total_cost': total_cost,
    }
    calculate_bill(service,prescribedmedicine)


    return render(request, 'bill/service_dropdown_list_options.html', {'medicine': service})


def generate_bill(request):
    return render(request,"bill/bill_detail.html",context)


def calculate_bill(service,prescribedmedicine):
    service_cost = 0.00
    medicine_cost = 0.00
    for s in service:
        service_cost = s.service.cost

    for pm in prescribedmedicine:
        medicine_cost += pm.medicine.price*pm.quantity




    # print("Service cost is ", service_cost)
    # print("Medicine cost is ", medicine_cost)

def generate_pdf(request):
    # paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
    # html_string = render_to_string('core/pdf_template.html', {'paragraphs': paragraphs})
    #
    # html = HTML(string=html_string)
    # html.write_pdf(target='/tmp/mypdf.pdf');
    #
    # fs = FileSystemStorage('/tmp')
    # with fs.open('mypdf.pdf') as pdf:
    #     response = HttpResponse(pdf, content_type='application/pdf')
    #     response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    #     return response

    pass



def check_prescription(request):

    prescription_id = request.GET.get('prescription')

    #
    # print(patient_id,doctor_id,appointment_schedule_id)
    data = {
        'is_taken': Bill.objects.filter(Q(prescription_id=prescription_id)).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Bill for this prescription is already done.'
    return JsonResponse(data)