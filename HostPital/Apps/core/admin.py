from django.contrib import admin
from .models import Doctor, Cliente, Enfermero

@admin.register(Doctor)
class doctorAd(admin.ModelAdmin):
    list_display = ('id', 'tipoUsuario', 'nombre', 'apellido', 'numeroDocumento', 'fechaNacimiento', 'telefono', 'disponible')
    list_filter = ('id', 'tipoUsuario', 'numeroDocumento')
    search_fields = ('id', 'numeroDocumento', 'tipoUsuario')
    readonly_fields = ('created','updated',)
    
@admin.register(Enfermero)
class enfermeroAd(admin.ModelAdmin):
    list_display = ('id', 'tipoUsuario', 'nombre', 'apellido', 'numeroDocumento', 'fechaNacimiento', 'telefono', 'activo')
    list_filter = ('id', 'tipoUsuario', 'numeroDocumento')
    search_fields = ('id', 'numeroDocumento', 'tipoUsuario')
    readonly_fields = ('created','updated',)

@admin.register(Cliente)
class clienteAd(admin.ModelAdmin):
    list_display = ('id', 'tipoUsuario', 'nombre', 'apellido', 'numeroDocumento', 'fechaNacimiento', 'telefono', 'activo')
    list_filter = ('id', 'tipoUsuario', 'numeroDocumento')
    search_fields = ('id', 'numeroDocumento', 'tipoUsuario')
    readonly_fields = ('created','updated',)
