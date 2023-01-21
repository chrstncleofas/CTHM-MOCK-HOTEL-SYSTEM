from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
    return render(request, 'LoginForm/login.html'),

def register(request):
    # form = UserCreationForm()
    return render(request, 'LoginForm/register.html'),
