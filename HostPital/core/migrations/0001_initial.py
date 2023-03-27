# Generated by Django 4.1.7 on 2023-03-27 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroDocumento', models.CharField(max_length=58)),
                ('nombre', models.CharField(max_length=48)),
                ('apellido', models.CharField(max_length=48)),
                ('fechaNacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=16)),
                ('tipoUsuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponible', models.BooleanField()),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.datosusuario')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEsp', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.datosusuario')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorEspecialista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField()),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.datosusuario')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('duracion', models.PositiveIntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.datosusuario')),
            ],
        ),
    ]
