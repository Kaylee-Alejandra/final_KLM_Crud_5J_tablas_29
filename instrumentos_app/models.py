from django.db import models

# Create your models here.
class Instrumento(models.Model):
    codigo= models.IntegerField(primary_key=True)
    tipo_instrumento= models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    marca=models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    nombre=models.CharField(max_length=100)
    tamaño=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre