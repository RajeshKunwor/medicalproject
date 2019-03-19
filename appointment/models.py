from django.db import models
from patient.models import *
from doctor.models import *
# Create your models here.


class Appointment(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="a_p")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="a_d")
    appointment_schedule = models.ForeignKey(DoctorSchedule, on_delete=models.CASCADE, related_name="doctor_schedule")
    status = models.CharField(max_length=20, default='')

    def __str__(self):
        return f'{self.patient} is appointed to {self.doctor} at {self.appointment_schedule}'

