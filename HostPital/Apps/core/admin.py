from django.contrib import admin
from .models import Doctor, Cliente, Enfermero

@admin.register(Doctor)
class doctorAd(admin.ModelAdmin):
    list_display = ('id', 'tipoUsuario', 'nombre', 'apellido', 'numeroDocumento', 'fechaNacimiento', 'telefono', 'disponible')

@admin.register(Enfermero)
class enfermeroAd(admin.ModelAdmin):
    list_display = ('id', 'tipoUsuario', 'nombre', 'apellido', 'numeroDocumento', 'fechaNacimiento', 'telefono', 'activo')

@admin.register(Cliente)
class clienteAd(admin.ModelAdmin):
    list_display = ('id', 'tipoUsuario', 'nombre', 'apellido', 'numeroDocumento', 'fechaNacimiento', 'telefono', 'activo')