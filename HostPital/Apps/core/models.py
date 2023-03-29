from django.db import models

# Create your models here.
class DatosUsuario(models.Model):
    
    tUser = (
        ('doctor', 'Doctor'),
        ('enfermero', 'Enfermero'),
        ('cliente', 'Cliente'),
    )
    
    tipoUsuario = models.CharField(max_length = 10, blank = False, null = False, choices = tUser, verbose_name = "Tipo usuario")
    numeroDocumento = models.CharField(max_length = 58, blank = False, null = False, verbose_name = 'Numero documento')
    nombre = models.CharField(max_length = 48, blank = False, null = False, verbose_name = 'Nombre')
    apellido = models.CharField(max_length = 48, blank = False, null = False, verbose_name = 'Apellido')
    fechaNacimiento = models.DateField(blank = False, null = False, verbose_name = 'Fecha de nacimiento')
    telefono = models.CharField(max_length = 16 ,blank = False, null = False, verbose_name = 'Telefono')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta():
        abstract = True

class Doctor(DatosUsuario):
    disponible = models.BooleanField(verbose_name = 'Disponible')
    
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctores'
        
        ordering = ['-created']
    
class Enfermero(DatosUsuario):
    activo = models.BooleanField(verbose_name = 'Activo')
    
    class Meta:
        verbose_name = 'Enfermero'
        verbose_name_plural = 'Enfermeros'
        
        ordering = ['-created']
    
class Cliente(DatosUsuario):
    activo = models.BooleanField(verbose_name = 'Activo')
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
        ordering = ['-created']