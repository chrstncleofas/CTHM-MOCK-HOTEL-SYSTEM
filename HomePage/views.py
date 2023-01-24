from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Reservation, Contact
# from .forms import Reservation_Form
from django.urls import reverse

# Create your views here.

def home(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contacts = Contact.objects.create()

        contacts.name = name
        contacts.email = email
        contacts.message = message

        contacts.save()

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
        # name = request.POST.get('name')
        new_fname = request.POST.get('fname')
        new_lname = request.POST.get('lname')
        new_address = request.POST.get('address')
        new_city = request.POST.get('city')
        new_province = request.POST.get('province')
        new_postal = request.POST.get('postal')
        new_email = request.POST.get('email')
        new_phone = request.POST.get('phone')
        arrival_date = request.POST.get('arrival_date')
        arrival_time = request.POST.get('arrival_time')
        departure_date = request.POST.get('departure_date')
        departure_time = request.POST.get('departure_time')
        number_person = request.POST.get('number_person')
        message = request.POST.get('message')

        reservation = Reservation.objects.create()

        # resident.name = name

        reservation.fname = new_fname
        reservation.lname = new_lname
        reservation.address = new_address
        reservation.city = new_city
        reservation.province = new_province
        reservation.postal = new_postal
        reservation.email = new_email
        reservation.phone = new_phone
        reservation.arrival_date = arrival_date
        reservation.arrival_time = arrival_time
        reservation.departure_date = departure_date
        reservation.departure_time = departure_time
        reservation.number_person = number_person
        reservation.message = message

        reservation.save()


        return render(request, 'HomePage/bookPage.html',{
            'form': Reservation(),
            'success': True
        })
    else:
        return render(request, 'HomePage/bookPage.html',{
            'form': Reservation(),
        })


def contact(request):
    return render(request, 'HomePage/contact.html')

