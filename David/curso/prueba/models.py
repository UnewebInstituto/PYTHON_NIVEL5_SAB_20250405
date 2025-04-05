from django.db import models

# Create your models here.
class Contactos(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    correo = models.CharField(max_length=250, unique=True)
    telefono = models.CharField(max_length=250)
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.correo} {self.telefono}"
