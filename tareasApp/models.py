from django.db import models

# Create your models here.

#CREACION DE MODELOS PARA LA BASE DE DATOS CON LAS SIGUIENTES PROPIEDADES
class tareas(models.Model):
    nombre = models.CharField(max_length=32, null=True, blank=True)
    descripcion = models.CharField(max_length=32, null=True, blank=True)
    fechaFin = models.CharField(max_length=32, null=True, blank=True)
    status = models.CharField(max_length=32, null=True, blank=True)
    responsable = models.CharField(max_length=32, null=True, blank=True)