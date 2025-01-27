from django.contrib.auth.models import AbstractUser
from django.db import models
from cars.models import Cars
from datetime import datetime

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

class Orders(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="customer")
    car = models.ForeignKey(Cars, on_delete=models.CASCADE,  related_name='car')
    address = models.TextField(blank=True, null=True)
    TRXid = models.CharField(max_length=30, default="Dues")
    orderedat = models.DateTimeField(default=datetime.now)
    totalamount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.car.brand} {self.car.model}"

