# Generated by Django 4.1.7 on 2023-03-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediosInternos', '0002_alter_cita_cliente_alter_cita_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialidad',
            name='nombreEsp',
            field=models.CharField(max_length=48, verbose_name='Nombre de especialidad'),
        ),
    ]
