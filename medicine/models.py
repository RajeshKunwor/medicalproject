from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    expiry_date = models.DateField()

    def __str__(self):
        return f'{self.name}'