from django.contrib import admin
from .models import DoctorEspecialista

# Register your models here.
@admin.register(DoctorEspecialista)
class doctorEspAd(admin.ModelAdmin):
    list_display = ('id', 'doctor_info', '_especialidad_')
    list_filter = ('doctor__apellido','especialidad__nombreEsp')