from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    # form = UserCreationForm()
    return render(request, 'register.html'),

def login(request):
    return render(request, 'login.html'),