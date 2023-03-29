# Generated by Django 4.1.7 on 2023-03-29 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoUsuario', models.CharField(choices=[('doctor', 'Doctor'), ('enfermero', 'Enfermero'), ('cliente', 'Cliente')], max_length=10)),
                ('numeroDocumento', models.CharField(max_length=58)),
                ('nombre', models.CharField(max_length=48)),
                ('apellido', models.CharField(max_length=48)),
                ('fechaNacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=16)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('activo', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoUsuario', models.CharField(choices=[('doctor', 'Doctor'), ('enfermero', 'Enfermero'), ('cliente', 'Cliente')], max_length=10)),
                ('numeroDocumento', models.CharField(max_length=58)),
                ('nombre', models.CharField(max_length=48)),
                ('apellido', models.CharField(max_length=48)),
                ('fechaNacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=16)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('disponible', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctores',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoUsuario', models.CharField(choices=[('doctor', 'Doctor'), ('enfermero', 'Enfermero'), ('cliente', 'Cliente')], max_length=10)),
                ('numeroDocumento', models.CharField(max_length=58)),
                ('nombre', models.CharField(max_length=48)),
                ('apellido', models.CharField(max_length=48)),
                ('fechaNacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=16)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('activo', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Enfermero',
                'verbose_name_plural': 'Enfermeros',
                'ordering': ['-created'],
            },
        ),
    ]
