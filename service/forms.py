from django import forms
from .models import *
import re

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_name(self):
       name = self.cleaned_data.get('name', '')
       rule = re.compile(r'^[A-Za-z]{1}')

       if not re.match(rule, name):
           raise forms.ValidationError("Invalid Name.")
       return self.cleaned_data.get('name', '')
