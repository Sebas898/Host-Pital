from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DatosUsuario(models.Model):
    tipoUsuario = models.OneToOneField(User, on_delete=models.CASCADE)
    numeroDocumento = models.CharField(max_length = 58, blank = False, null = False)
    nombre = models.CharField(max_length = 48, blank = False, null = False)
    apellido = models.CharField(max_length = 48, blank = False, null = False)
    fechaNacimiento = models.DateField(blank = False, null = False)
    telefono = models.CharField(max_length = 16 ,blank = False, null = False)
    
class Admin(models.Model):
    perfil = models.OneToOneField(DatosUsuario, on_delete=models.CASCADE)

class Doctor(models.Model):
    perfil = models.OneToOneField(DatosUsuario, on_delete=models.CASCADE)
    disponible = models.BooleanField()

class Especialidad(models.Model):
    nombreEsp = models.CharField(max_length = 48, blank = False, null = False)

class DoctorEspecialista(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete = models.CASCADE)
    
class Enfermero(models.Model):
    perfil = models.OneToOneField(DatosUsuario, on_delete = models.CASCADE)
    
class Cliente(models.Model):
    perfil = models.OneToOneField(DatosUsuario, on_delete=models.CASCADE)
    activo = models.BooleanField()
    
class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    fecha = models.DateField(blank = False, null = False)
    duracion = models.PositiveIntegerField()
    
# class Cita(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
#     fecha = models.DateTimeField(blank = False, null = False)
#     duracion = models.PositiveIntegerField()