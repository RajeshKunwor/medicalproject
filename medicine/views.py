from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user.decorators import *
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
@method_decorator([login_required(login_url='login'), group_required('Staff')],name='dispatch')
class MedicineCreateView(CreateView):
    model = Medicine
    form_class = MedicineForm
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Medicine is successfully Added.')
        return redirect('medicine:medicine_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


@method_decorator([login_required(login_url='login'), group_required('Staff')],name='dispatch')
class MedicineUpdateView(UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Medicine is successfully Updated.')
        return redirect('medicine:medicine_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


@method_decorator([login_required(login_url='login'), group_required('Staff','Reciepnist')],name='dispatch')
class MedicineListView(ListView):
    model = Medicine
    paginate_by = 5
    context_object_name = 'medicine'