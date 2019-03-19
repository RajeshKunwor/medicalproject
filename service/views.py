from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user.decorators import *
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
@method_decorator([login_required(login_url='login'), group_required('Staff')],name='dispatch')
class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Service is successfully Added.')
        return redirect('service:service_list')
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))



@method_decorator([login_required(login_url='login'), group_required('Staff')],name='dispatch')
class ServiceUpdateView(UpdateView,SuccessMessageMixin):
    model = Service
    form_class = ServiceForm
    success_message = "Service is successfully Updated."
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Service is successfully Updated.',extra_tags='alert')
        return redirect('service:service_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


@method_decorator([login_required(login_url='login'), group_required('Staff','Reciepnist')],name='dispatch')
class ServiceListView(ListView):
    model = Service
    paginate_by = 5
    context_object_name = 'service'


@method_decorator([login_required(login_url='login'), group_required('Staff')],name='dispatch')
class ServiceDeleteView(DeleteView):
    model = Service
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('service:service_list')