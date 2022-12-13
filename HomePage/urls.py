from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('accomodation/', views.accomodation, name='accomodation'),
    path('gallery/', views.gallery, name='gallery'),
    path('addroom/', views.addroom, name='addroom'),
    path('bookPage/', views.bookPage, name='bookPage'),
    path('contact/', views.contact, name='contact'),
]