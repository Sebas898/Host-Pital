from django.db import models
from Apps.core.models import Cliente, Doctor
from datetime import timedelta

# Create your models here.
class Duracion(models.DurationField):
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return timedelta(seconds=value.total_seconds())

    def to_python(self, value):
        if isinstance(value, timedelta):
            return value
        if isinstance(value, str):
            try:
                hours, minutes, seconds = map(int, value.split(':'))
                return timedelta(hours=hours, minutes=minutes, seconds=seconds)
            except ValueError:
                pass
        return super().to_python(value)

    def get_prep_value(self, value):
        if value is None:
            return None
        return value.total_seconds()

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, verbose_name = 'Nombre cliente')
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, verbose_name = 'Nombre doctor')
    fecha = models.DateField(blank = False, null = False, verbose_name = 'Fecha')
    duracion = Duracion(help_text = 'Duración en formato hh:mm:ss', default = timedelta(hours = 0))
    
    def cliente_info(self):
        return f'({self.cliente.id}) {self.cliente.nombre} {self.cliente.apellido}'

    def doctor_info(self):
        return f'({self.doctor.id}) {self.doctor.nombre} {self.doctor.apellido}'
    
class Especialidad(models.Model):
    nombreEsp = models.CharField(max_length = 48, blank = False, null = False, verbose_name = 'Nombre de especialidad')