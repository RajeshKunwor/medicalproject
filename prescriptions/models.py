from django.db import models
from patient.models import*
from doctor.models import *
from service.models import Service
from observation.models import Observation
from medicine.models import Medicine

# Create your models here.

class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    observation = models.ForeignKey(Observation,on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.id}'


class PrescribedMedicine(models.Model):
    prescription = models.ForeignKey(Prescription,on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f'{self.id}'
