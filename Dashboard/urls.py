from django.urls import path
from Dashboard import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]