from django.contrib import admin
from .models import DoctorEspecialista

# Register your models here.
@admin.register(DoctorEspecialista)
class doctorEspAd(admin.ModelAdmin):
    list_display = ('id', 'get_doctor_info', 'get_especialidad')