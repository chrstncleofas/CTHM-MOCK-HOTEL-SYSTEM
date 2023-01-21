from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'Dashboard/index.html')

def login(request):
    return render(request, 'Dashboard/login.html')

def register(request):
    return render(request, 'Dashboard/register.html')