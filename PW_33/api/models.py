
# Create your models here.
from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    fundacion = models.CharField(max_length=50)
    apodo = models.CharField(max_length=30)
    estadio = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
