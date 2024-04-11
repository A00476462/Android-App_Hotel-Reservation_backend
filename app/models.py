from django.db import models

# Create your models here.

class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False, default=0.0)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    availability = models.BooleanField(default=False)

class Reservation(models.Model):
    reservation_id = models.BigAutoField(primary_key=True)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

class Guest(models.Model):
    guest_id = models.BigAutoField(primary_key=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    email = models.CharField(max_length=200)