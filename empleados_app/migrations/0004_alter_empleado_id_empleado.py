# Generated by Django 5.1.2 on 2024-11-29 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados_app', '0003_remove_empleado_color_remove_empleado_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='id_empleado',
            field=models.IntegerField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
