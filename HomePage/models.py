from django.db import models

# Create your models here.
class Reservation(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    province = models.CharField(max_length=70)
    postal = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    arrival_date = models.CharField(max_length=50)
    arrival_time = models.CharField(max_length=50)
    departure_date = models.CharField(max_length=50)
    departure_time = models.CharField(max_length=50)
    number_person = models.CharField(max_length=50)
    message = models.CharField(max_length=80)

    def __str__(self):
        return f'Reservation: {self.fname} {self.lname}'

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=100)

    def __str__(self):
        return f'Reservation: {self.name}'
