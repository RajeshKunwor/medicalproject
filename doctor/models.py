from django.db import models
from location.models import *
from django.contrib.auth.models import User
ethical_group = (
    ('Dalit','Dalit'),('Janjati','Janjati'),('Madeshi','Madeshi'),('Muslin','Muslin'),
    ('Bhraman/Chetri','Bhraman/Chetri'),('Ohter','Other')

)

sex = (('Male','Male'),('Female','Female'),('Other','Other'))
region =(('Physiciaan','Physiciaan'),('Cardiologist','Cardiologist'),('Gastroenterologist','Gastroenterologist'),('Allergists/Immunologist','Allergists/Immunologist'),
('Anesthesiologist','Anesthesiologist'),('Colon and Rectal Surgeon','Colon and Rectal Surgeon'),('Endocrinologist','Endocrinologist'),('Dermatologist','Dermatologist'))

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, verbose_name='First Name')
    middle_name = models.CharField(max_length=20, verbose_name='Middle Name',null= True,blank=True)
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    specialist = models.CharField(choices=region,max_length=100)
    ethical_group = models.CharField(choices=ethical_group, verbose_name='Ethical Group', max_length=50,null= True,blank=True)
    sex = models.CharField(choices=sex, verbose_name='Sex', max_length=15)
    age = models.IntegerField(verbose_name='Age')
    email = models.EmailField(max_length=50,default='',blank=True)
    citizenship_number = models.CharField(verbose_name='Citizenship Number',default='', max_length=50,unique=True,blank=True)
    mobile_no = models.CharField(verbose_name="Mobile No.", max_length=15)
    phone_no = models.CharField(verbose_name='Phone No.',default='', max_length=10,blank=True)
    p_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='dperma', verbose_name='Province')
    p_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='dperma', verbose_name="District")
    p_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, related_name='dperma',
                                       verbose_name="Municipality/VDC")
    p_ward_no = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='dperma', verbose_name="Ward No.")
    p_street = models.CharField(max_length=50, verbose_name="Street")
    t_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='dtemp', verbose_name="Province")
    t_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='dtemp', verbose_name="District")
    t_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, related_name='dtemp',
                                       verbose_name="Municipality/VDC")
    t_ward_no = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='dtemp', verbose_name="Ward No.")
    t_street = models.CharField(max_length=50, verbose_name="Street")

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


shift=(('Morining','Morning'),('Evening','Evening'),('Day','Day'))

class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name='doctor_schedule')
    date = models.DateField()
    time = models.CharField(max_length=20)
    shift = models.CharField(choices=shift, max_length=15)
    max_patient = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.date }/{self.time }/{self.shift}'

