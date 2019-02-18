from django import forms
from .models import *

class ObservationForm(forms.ModelForm):

    class Meta:
        model = Observation
        exclude = ['patient']

