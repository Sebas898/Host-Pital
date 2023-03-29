from django.db import models

# Create your models here.
class DatosUsuario(models.Model):
    
    tUser = (
        ('doctor', 'Doctor'),
        ('enfermero', 'Enfermero'),
        ('cliente', 'Cliente'),
    )
    
    tipoUsuario = models.CharField(max_length = 10, blank = False, null = False, choices = tUser)
    numeroDocumento = models.CharField(max_length = 58, blank = False, null = False)
    nombre = models.CharField(max_length = 48, blank = False, null = False)
    apellido = models.CharField(max_length = 48, blank = False, null = False)
    fechaNacimiento = models.DateField(blank = False, null = False)
    telefono = models.CharField(max_length = 16 ,blank = False, null = False)
    
    class Meta():
        abstract = True

class Doctor(DatosUsuario):
    disponible = models.BooleanField()
    
class Enfermero(DatosUsuario):
    activo = models.BooleanField()
    
class Cliente(DatosUsuario):
    activo = models.BooleanField()