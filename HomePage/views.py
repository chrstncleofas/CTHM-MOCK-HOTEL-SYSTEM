from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'HomePage/home.html')

def login(request):
    return render(request, 'HomePage/login.html')

def register(request):
    return render(request, 'HomePage/register.html')

def listroom(request):
    return render(request, 'HomePage/listroom.html')

def gallery(request):
    return render(request, 'HomePage/gallery.html')

