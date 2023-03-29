from django.db import models
from Apps.core.models import Doctor
from Apps.mediosInternos.models import Especialidad

# Create your models here.
class DoctorEspecialista(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete = models.CASCADE)

    def get_doctor_info(self):
        return f'({self.doctor.id}) {self.doctor.nombre} {self.doctor.apellido}'
    
    def get_especialidad(self):
        return self.especialidad.nombreEsp