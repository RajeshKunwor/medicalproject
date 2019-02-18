from django.db import models
from patient.models import *
from doctor.models import *
# Create your models here.

shift=(('Morining','Morining'),('Evening','Evening'),('Day','Day'))

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="a_p")
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="a_d")
    appointment_date = models.DateField( default='')
    appointment_time = models.TimeField(default='')
    shift = models.CharField(choices=shift,max_length=15,default='')

    def __str__(self):
        return self.patient +'with' +self.doctor+'at'+self.appointment_time

