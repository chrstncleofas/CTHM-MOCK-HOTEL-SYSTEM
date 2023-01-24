# from django import forms
# from .models import Reservation


# class Reservation_Form(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ['fname', 'lname', 'address', 'city', 'province', 'postal', 'birthday', 'gender', 'email', 'phone']
#         labels = {
#             'fname': 'First Name', 
#             'lname': 'Last Name', 
#             'address': 'Address', 
#             'city': 'City', 
#             'province': 'Province', 
#             'postal': 'Postal', 
#             'birthday': 'Birthday', 
#             'gender': 'Gender', 
#             'email': 'Email', 
#             'phone': 'Phone',
#         }
#         widgets = {
#             'fname': forms.TextInput(attrs={'class': 'form-control'}), 
#             'lname': forms.TextInput(attrs={'class': 'form-control'}), 
#             'address': forms.TextInput(attrs={'class': 'form-control'}), 
#             'city': forms.TextInput(attrs={'class': 'form-control'}), 
#             'province': forms.TextInput(attrs={'class': 'form-control'}), 
#             'postal': forms.TextInput(attrs={'class': 'form-control'}), 
#             'birthday': forms.TextInput(attrs={'class': 'form-control'}), 
#             'gender': forms.TextInput(attrs={'class': 'form-control'}), 
#             'email': forms.TextInput(attrs={'class': 'form-control'}), 
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#         }