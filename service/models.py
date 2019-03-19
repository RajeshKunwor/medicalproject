from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100,unique=True)
    cost = models.FloatField()


    # def clean(self):
    #     if self.name.isalnum() == False:
    #         raise ValidationError("Invalid Name")
    #

    def __str__(self):
        return f'{self.name}'
