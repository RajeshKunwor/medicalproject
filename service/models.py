from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField(default=0.00)


    # def clean(self):
    #     if self.name.isalnum() == False:
    #         raise ValidationError("Invalid Name")
    #

    def __str__(self):
        return self.name
