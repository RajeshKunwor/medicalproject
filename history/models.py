from django.db import models
from patient.models import Patient
# Create your models here.

class History(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    details = models.TextField()

    def __str__(self):
        return self.patient
