from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

# Create your models here.
class DatosUsuario(models.Model):
    
    numeroDocumento = models.CharField(max_length = 58, blank = False, null = False, verbose_name = 'Numero documento')
    nombre = models.CharField(max_length = 48, blank = False, null = False, verbose_name = 'Nombre')
    apellido = models.CharField(max_length = 48, blank = False, null = False, verbose_name = 'Apellido')
    fechaNacimiento = models.DateField(blank = False, null = False, verbose_name = 'Fecha de nacimiento')
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True,  verbose_name='Correo electrónico')
    password = models.CharField(max_length = 128, blank=False, null=False, verbose_name='Contraseña')
    telefono = models.CharField(max_length = 16 ,blank = False, null = False, verbose_name = 'Telefono')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    def save(self, *args, **kwargs):
        # encriptar la contraseña antes de guardar
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    
    class Meta():
        abstract = True

class Doctor(DatosUsuario):
    tipoUsuario = models.CharField(max_length = 10, blank = False, null = False, default = 'Doctor', verbose_name = "Tipo usuario")
    disponibleParaCitas = models.BooleanField(verbose_name = 'Disponible para citas')
    
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctores'
        
        ordering = ['-created']
    
class Enfermero(DatosUsuario):
    tipoUsuario = models.CharField(max_length = 10, blank = False, null = False, default = 'Enfermero', verbose_name = "Tipo usuario")
    trabajandoEnHospital = models.BooleanField(verbose_name = 'Trabajando en hospital')
    
    class Meta:
        verbose_name = 'Enfermero'
        verbose_name_plural = 'Enfermeros'
        
        ordering = ['-created']
    
class Cliente(DatosUsuario):
    tipoUsuario = models.CharField(max_length = 10, blank = False, null = False, default = 'Cliente', verbose_name = "Tipo usuario")
    activo = models.BooleanField(verbose_name = 'Activo')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
        ordering = ['-created']