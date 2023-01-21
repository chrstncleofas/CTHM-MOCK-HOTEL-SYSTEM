from django.urls import path
from Dashboard import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]