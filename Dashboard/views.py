from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from HomePage.models import Reservation, Contact
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def main_page(request):
    return render(request, 'Dashboard/index.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            # fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            # return render(request, 'authentication/dashboard.html')
            # return render(request, "authentication/dashboard.html",{"fname":fname})
            return redirect('dashboard')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('main_page')

    return render(request, 'Dashboard/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        # myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        return redirect('login_page')

    return render(request, 'Dashboard/register.html')

def dashboard(request):
    return render(request, 'Dashboard/dashboard.html', {
        'reservation': Reservation.objects.all(),
        'contact': Contact.objects.all(),
    })

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('main_page')


def list(request):
    return render(request, 'Dashboard/list.html', {
        'reservation' : Reservation.objects.all(),
    })

def list_item(request, id):
    reservations = Reservation.objects.get(pk=id)
    return HttpResponseRedirect(reverse('list'))

def edit_list(request, id):
    if request.method == 'POST':
        reservation = Reservation.objects.get(pk=id)
        form = Reservation(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return render(request, 'Dashboard/edit.html', {
                'form': form,
                'success': True,
            })
    else:
        reservation = Reservation.objects.get(pk=id)
        form = Reservation(instance=reservation)
    return render(request, 'Dashboard/edit.html',{
        'form': form,
    })

def delete_list(request, id):
    if request.method == 'POST':
        reservation = Reservation.objects.get(pk=id)
        reservation.delete()
    return HttpResponseRedirect(reverse('list'))