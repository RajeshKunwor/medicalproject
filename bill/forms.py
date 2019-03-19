from django import forms
from .models import *
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        exclude =['patient']


