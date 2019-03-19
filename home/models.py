from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notification(models.Model):

    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_user')
    message = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_user')
    date = models.DateField()
    time = models.TimeField()


