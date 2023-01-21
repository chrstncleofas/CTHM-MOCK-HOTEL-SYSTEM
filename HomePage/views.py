from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Reservation
from .forms import Reservation_Form
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'HomePage/home.html')

def login(request):
    return render(request, 'HomePage/login.html')

def register(request):
    return render(request, 'HomePage/register.html')

def accomodation(request):
    return render(request, 'HomePage/accomodation.html')

def gallery(request):
    return render(request, 'HomePage/gallery.html')

def addroom(request):
    return render(request, 'HomePage/roomAdd.html')

def bookPage(request):
    if request.method == 'POST':
        form = Reservation_Form(request.POST)
        if form.is_valid():

            new_fname = form.cleaned_data['fname']
            new_lname = form.cleaned_data['lname']
            new_address = form.cleaned_data['address']
            new_city = form.cleaned_data['city']
            new_province = form.cleaned_data['province']
            new_postal = form.cleaned_data['postal']
            new_birthday = form.cleaned_data['birthday']
            new_gender = form.cleaned_data['gender']
            new_email = form.cleaned_data['email']
            new_phone = form.cleaned_data['phone']

            new_reservation = Reservation(
                fname = new_fname,
                lname = new_lname,
                address = new_address,
                city = new_city,
                province = new_province,
                postal = new_postal,
                birthday = new_birthday,
                gender = new_gender,
                email = new_email,
                phone = new_phone,
            )

            new_reservation.save()

    return render(request, 'HomePage/bookPage.html',{
        'form': Reservation_Form(),
        'success': True
    })


def contact(request):
    return render(request, 'HomePage/contact.html')

