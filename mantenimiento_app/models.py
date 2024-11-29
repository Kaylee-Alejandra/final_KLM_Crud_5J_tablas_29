from django.db import models

# Create your models here.
class Mantenimiento(models.Model):
    id_mantenimiento= models.IntegerField(primary_key=True)
    horarios = models.CharField(max_length=100)
    pisos= models.CharField(max_length=100)
    instrumentos=models.CharField(max_length=100)
    oficinas=models.CharField(max_length=100)
    empleados = models.CharField(max_length=100)
    materiales=models.CharField(max_length=100)

    def __str__(self):
        return self.id_mantenimiento