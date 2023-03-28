from django.db import models
from Apps.core.models import Cliente, Doctor

# Create your models here.
class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    fecha = models.DateField(blank = False, null = False)
    duracion = models.PositiveIntegerField()
    
    def get_cliente_info(self):
        return f'({self.cliente.id}) {self.cliente.nombre} {self.cliente.apellido}'

    def get_doctor_info(self):
        return f'({self.doctor.id}) {self.doctor.nombre} {self.doctor.apellido}'
    
class Especialidad(models.Model):
    nombreEsp = models.CharField(max_length = 48, blank = False, null = False)