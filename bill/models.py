from django.db import models
from patient.models import Patient
from observation.models import Observation
from service.models import Service
from prescriptions.models import Prescription, PrescribedMedicine

# Create your models here.
class Bill(models.Model):

    date = models.DateField()
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="bill_patient")
    prescription = models.OneToOneField(Prescription,on_delete=models.CASCADE,related_name='bill_prescription')
    # medicine = models.ForeignKey(Service,on_delete=models.CASCADE, related_name="bill_service")
    # prescribed_medicine = models.ForeignKey(PrescribedMedicine,on_delete=models.CASCADE,related_name="bill_prescribed_medicine")
