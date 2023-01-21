from django.shortcuts import render
from HomePage.models import Reservation

# Create your views here.

def main_page(request):
    return render(request, 'Dashboard/index.html',{
        'reservation': Reservation.objects.all(),
    })

def login(request):
    return render(request, 'Dashboard/login.html')

def register(request):
    return render(request, 'Dashboard/register.html')

def dashboard(request):
    return render(request, 'Dashboard/dashboard.html')