from django import forms
from .models import Reservation

class Reservation_Form(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['fname', 'lname', 'address', 'city', 'province', 'postal', 'birthday', 'gender', 'email', 'phone']
        labels = {
            'fname': 'First Name', 
            'lname': 'Last Name', 
            'address': 'Address', 
            'city': 'City', 
            'province': 'Province', 
            'postal': 'Postal', 
            'birthday': 'Birthday', 
            'gender': 'Gender', 
            'email': 'Email', 
            'phone': 'Phone',
        }