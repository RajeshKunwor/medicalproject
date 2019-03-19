from django import forms
from .models import *
from observation.models import Observation

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        exclude=['patient']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['observation'].queryset = Observation.objects.none()

        if 'patient' in self.data:
            try:
                patient_id = int(self.data.get('patient'))
                self.fields['observation'].queryset = Observation.objects.filter(patient_id=patient_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['observation'].queryset = Observation.objects.none()

class DemoForm(forms.ModelForm):
    class Meta:
        model = PrescribedMedicine
        exclude = ['prescription']


class PrescribedMedicineForm(forms.ModelForm):
    class Meta:
        model = PrescribedMedicine
        exclude =['prescription']