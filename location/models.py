from django.db import models

# Create your models here.
class Province(models.Model):
    province = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.province


class District(models.Model):
    province = models.ForeignKey(Province,on_delete=models.CASCADE,verbose_name="Province")
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