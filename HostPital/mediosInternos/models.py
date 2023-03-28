from django.db import models
from core.models import Cliente, Doctor

# Create your models here.
class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    fecha = models.DateField(blank = False, null = False)
    duracion = models.PositiveIntegerField()
    
class Especialidad(models.Model):
    nombreEsp = models.CharField(max_length = 48, blank = False, null = False)