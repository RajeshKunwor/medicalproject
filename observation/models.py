from django.db import models
from patient.models import Patient
from doctor.models import Doctor
# Create your models here.

class Observation(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

    # doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    BP = models.CharField(max_length=10)
    temperature = models.FloatField(blank=True)
    sugar = models.IntegerField(blank=True)
    comment = models.TextField(max_length=300)
    create_date = models.DateField()

    def __str__(self):
        return f'{self.id}'