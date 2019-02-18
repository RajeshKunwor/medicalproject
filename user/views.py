from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.views import generic
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .decorators import *
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.



@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class UserView(generic.ListView):
    model = User
    fields = ('username','is_active')
    context_object_name = 'user'


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class GroupView(generic.ListView):
    model = Group

    context_object_name = 'group'



@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class UserUpdateView(generic.UpdateView,SuccessMessageMixin):
    model =User
    form_class = UserRegistrationForm

    template_name_suffix = '_update_form'
    success_message = "%(username)sUser Successfully Updated."
    success_url= reverse_lazy('user:user_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class GroupUpdateView(generic.UpdateView):
    model = Group
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('user:group_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class UserDeleteView(generic.DeleteView):
    model = User
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('user:user_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class GroupDeleteView(generic.DeleteView):
    model = Group
    template_name_suffix = '_confrim_delete'
    success_url = reverse_lazy('user:group_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class UserCreationView(generic.CreateView):
    model = User
    #fields = ('username','email','password1','password2')
    form_class = UserRegistrationForm


    success_url =reverse_lazy('user:user_list')


@method_decorator([login_required(login_url='login'),superuser_only],name='dispatch')
class GroupCreationView(generic.CreateView,SuccessMessageMixin):
    model = Group
    fields = ['name']
    success_url = reverse_lazy('user:group_list')
    success_message = "%(name)s was created successfully"

@login_required(login_url='login')
@superuser_only
def add_user_to_group(request):
    user_id = request.POST['user']
    group_id = request.POST['group']
    user =User.objects.get(pk=user_id)
    group = Group.objects.get(pk=group_id)
    user.groups.add(group)
    return redirect('dashboard')

@login_required(login_url='login')
@superuser_only
def add_user_group(request):
    user = User.objects.all()
    group = Group.objects.all()

    context ={
        'user':user,
        'group':group,

    }
    return render(request,"user/usergroup1.html",context)
    #user.groups.add(group)






@login_required(login_url='login')
@superuser_only
def add_permission_group(request):
    perm = Permission.objects.all()
    group = Group.objects.all()

    context = {
        'perm': perm,
        'group': group,

    }
    return render(request, "DemoApp/grouppermission.html", context)




@login_required(login_url='login')
@superuser_only
def add_permission_to_group(request):
    perm_id = request.POST['perm']
    group_id = request.POST['group']
    perm =Permission.objects.get(pk=perm_id)
    group = Group.objects.get(pk=group_id)
    group.permissions.add(perm)
    return redirect('dashboard')


# @login_required(login_url='login')
# @permission_required('add_permission',raise_exception=True)
# @group_required('student')
# def show_msg(request):
#     return HttpResponse("Hi")