from django import forms
from .models import *

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields ='__all__'

class DemoForm(forms.ModelForm):
    class Meta:
        model = PrescribedMedicine
        exclude = ['prescription']


class PrescribedMedicineForm(forms.ModelForm):
    class Meta:
        model = PrescribedMedicine
        exclude =['prescription']