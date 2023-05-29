from django.db import models

# Create your models here.

class Libro(models.Model):
    nombre = models.CharField('Nombre', max_length=100,)
    descripcion = models.CharField('Descripcion', max_length=100, null=False, blank=False)