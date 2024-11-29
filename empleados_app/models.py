from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado= models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    puesto= models.CharField(max_length=100)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    telefono= models.IntegerField(null=False)
    correo= models.EmailField(null=False)

    def __str__(self):
        return self.nombre