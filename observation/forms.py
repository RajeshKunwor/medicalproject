from django import forms
from django.forms import DateInput
from .models import *

class ObservationForm(forms.ModelForm):

    class Meta:
        model = Observation
        exclude = ['patient']
        widgets = {
            'create_date': DateInput(attrs={'type': 'date'})
        }

