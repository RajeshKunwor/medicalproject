from django.db import models

ethical_group = (
    ('Dalit','Dalit'),('Janjati','Janjati'),('Madeshi','Madeshi'),('Muslin','Muslin'),
    ('Bhraman/Chetri','Bhraman/Chetri'),('Ohter','Other')

)

sex = (('Male','Male'),('Female','Female'),('Other','Other'))

# Create your models here.

class Province(models.Model):
    province = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.province


class District(models.Model):
    provice = models.ForeignKey(Province,on_delete=models.CASCADE,verbose_name="Province")
    district = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.district


class Municipality(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    municipality = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.municipality


class Ward(models.Model):
    municipality = models.ForeignKey(Municipality,on_delete=models.CASCADE)
    ward_no = models.IntegerField(verbose_name="Ward No.",unique=False)

    def __str__(self):
        return str(self.ward_no)


class Patient(models.Model):
    first_name = models.CharField(max_length=20,verbose_name='First Name')
    middle_name = models.CharField(max_length=20,verbose_name='Middle Name')
    last_name = models.CharField(max_length=20,verbose_name='Last Name')
    ethical_group = models.CharField(choices=ethical_group,verbose_name='Ethical Group',max_length=50)
    sex = models.CharField(choices=sex,verbose_name='Sex',max_length=15)
    age = models.IntegerField(verbose_name='Age')
    year_of_birth = models.DateField(verbose_name='Year Of Birth')
    citizenship_number = models.CharField(verbose_name='Citizenship Number',max_length=50)
    mobile_no = models.CharField(verbose_name="Mobile No.",max_length=15)
    phone_no = models.CharField(verbose_name='Phone No.',max_length=10)
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




class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    province = models.OneToOneField(Province, on_delete=models.SET_NULL, null=True,related_name="p")
    district = models.OneToOneField(District, on_delete=models.SET_NULL, null=True,related_name="d")

    def __str__(self):
        return self.name


class ServiceType(models.Model):
    service_type = models.CharField(max_length=50,verbose_name="Service Type")

    def __str__(self):
        return self.service_type


class PatientService(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType,on_delete=models.CASCADE)
    cost =models.FloatField(default=0.0)
    height = models.FloatField()
    weight = models.FloatField()
    BP = models.CharField(max_length=10)
    temperature = models.FloatField()
    sugar = models.IntegerField()
    comment = models.TextField(max_length=300)
    create_date = models.DateField()



class Medicine(models.Model):
    name = models.CharField(max_length=100,verbose_name="Medicine Name")



class Doctor(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='First Name')
    middle_name = models.CharField(max_length=20, verbose_name='Middle Name')
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    ethical_group = models.CharField(choices=ethical_group, verbose_name='Ethical Group', max_length=50)
    sex = models.CharField(choices=sex, verbose_name='Sex', max_length=15)
    age = models.IntegerField(verbose_name='Age')
    year_of_birth = models.DateField(verbose_name='Year Of Birth')
    citizenship_number = models.CharField(verbose_name='Citizenship Number', max_length=50)
    mobile_no = models.CharField(verbose_name="Mobile No.", max_length=15)
    phone_no = models.CharField(verbose_name='Phone No.', max_length=10)
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





class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()


    def __str__(self):
        return f'{self.doctor}|{self.schedule_date}|{self.schedule_time}'

