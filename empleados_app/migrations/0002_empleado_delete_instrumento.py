# Generated by Django 5.1 on 2024-11-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('puesto', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Instrumento',
        ),
    ]
