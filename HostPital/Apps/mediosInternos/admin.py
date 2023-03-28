from django.contrib import admin
from .models import Cita, Especialidad

# Register your models here.
@admin.register(Cita)
class citaAd(admin.ModelAdmin):
    list_display = ('get_cliente_info', 'get_doctor_info', 'fecha', 'duracion')

@admin.register(Especialidad)
class especialidadAd(admin.ModelAdmin):
    list_display = ('id', 'nombreEsp')