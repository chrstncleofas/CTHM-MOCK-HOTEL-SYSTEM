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
    return render(request, 'HomePage/bookPage.html')

def contact(request):
    return render(request, 'HomePage/contact.html')

