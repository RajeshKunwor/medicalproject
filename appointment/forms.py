from django import forms
from .models import Appointment
from doctor.models import *
from doctor.models import *
class AppointmentForm(forms.ModelForm):


    class Meta:
        model=Appointment
        exclude=['patient','status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['appointment_schedule'].queryset = DoctorSchedule.objects.none()

        if 'doctor' in self.data:
            try:
                doctor_id = int(self.data.get('doctor'))
                self.fields['appointment_schedule'].queryset = DoctorSchedule.objects.filter(doctor_id=doctor_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['appointment_schedule'].queryset = DoctorSchedule.objects.none()