from django.db import models
from location.models import *
from django.core.exceptions import ValidationError
import re
from service.models import Service
from doctor.models import Doctor
from django.contrib.auth.models import User
ethical_group = (
    ('Dalit','Dalit'),('Janjati','Janjati'),('Madeshi','Madeshi'),('Muslin','Muslin'),
    ('Bhraman/Chetri','Bhraman/Chetri'),('Ohter','Other')

)

sex = (('Male','Male'),('Female','Female'),('Other','Other'))
# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,verbose_name='First Name')
    middle_name = models.CharField(max_length=20,verbose_name='Middle Name',default='',blank=True)
    last_name = models.CharField(max_length=20,verbose_name='Last Name')
    ethical_group = models.CharField(choices=ethical_group,verbose_name='Ethical Group',max_length=50,default='',blank=True)
    sex = models.CharField(choices=sex,verbose_name='Sex',max_length=15)
    age = models.IntegerField(verbose_name='Age')
    # year_of_birth = models.DateField(verbose_name='Year Of Birth')
    citizenship_number = models.CharField(verbose_name='Citizenship Number',default='',max_length=50,blank=True,unique=True)
    email= models.EmailField(max_length=50,default='',blank=True)
    mobile_no = models.CharField(verbose_name="Mobile No.",max_length=15)
    phone_no = models.CharField(verbose_name='Phone No.',default='',max_length=10,blank=True)
    p_province = models.ForeignKey(Province,on_delete=models.CASCADE,related_name='perma',verbose_name='Province')
    p_district = models.ForeignKey(District,on_delete=models.CASCADE,related_name='perma',verbose_name="District")
    p_municipality = models.ForeignKey(Municipality,on_delete=models.CASCADE,related_name='perma',verbose_name="Municipality/VDC")
    p_ward_no = models.ForeignKey(Ward,on_delete=models.CASCADE,related_name='perma',verbose_name="Ward No.")
    p_street = models.CharField(max_length=50,verbose_name="Street")
    t_province = models.ForeignKey(Province,on_delete=models.CASCADE,related_name='temp',verbose_name="Province")
    t_district = models.ForeignKey(District,on_delete=models.CASCADE,related_name='temp',verbose_name="District")
    t_municipality = models.ForeignKey(Municipality,on_delete=models.CASCADE,related_name='temp',verbose_name="Municipality/VDC")
    t_ward_no = models.ForeignKey(Ward ,on_delete=models.CASCADE,related_name='temp',verbose_name="Ward No.")
    t_street = models.CharField(max_length=50,verbose_name="Street")




    def __str__(self):
        return f'{self.user} | {self.first_name} {self.last_name}'





class PatientVisit(models.Model):

    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    BP = models.CharField(max_length=10)
    temperature = models.FloatField(blank=True)
    sugar = models.IntegerField(blank=True)
    comment = models.TextField(max_length=300)
    create_date = models.DateField()

    def __str__(self):
        return f'{self.patient}|{self.medicine}|{self.create_date}'