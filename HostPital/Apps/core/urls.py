from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('registro/', views.register, name = 'registro'),
    path('login/', views.login, name = 'login'),
]