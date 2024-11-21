from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    minimum_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
