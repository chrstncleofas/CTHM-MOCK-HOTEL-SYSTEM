from django.db import models

# Create your models here.
class Reservation(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    province = models.CharField(max_length=70)
    postal = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f'Reservation: {self.fname} {self.lname}'
    