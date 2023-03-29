# Generated by Django 4.1.7 on 2023-03-29 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_alter_cliente_tipousuario_alter_doctor_tipousuario_and_more'),
        ('mediosInternos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorEspecialista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediosInternos.especialidad')),
            ],
        ),
    ]
