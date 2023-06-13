from django.db import models

class Cliente(models.Model):
    razon_social = models.CharField(max_length=40)
    cuit = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return f"Razon Social: {self.razon_social}"

class Proveedor(models.Model):
    razon_social = models.CharField(max_length=40)
    cuit = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return f"Razon Social: {self.razon_social}"

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return f"Razon Social: {self.nombre}"


