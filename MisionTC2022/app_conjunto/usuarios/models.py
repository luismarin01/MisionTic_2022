from django.db import models

# Create your models here.
class Tipo_Usuario(models.Model):
    codigo_usuario = models.CharField(max_length=128, primary_key=True)
    tipo_usuario = models.TextField(max_length=128)

class Usuario(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombres = models.TextField(max_length=128)
    apellidos = models.TextField(max_length=128)
    torre = models.IntegerField
    apartamento = models.IntegerField
    email = models.TextField(max_length=128)
    telefono = models.IntegerField
    codigo_usuario = models.IntegerField

class Servicios(models.Model):
    fecha = models.DateField
    tipo_servicio = models.IntegerField
    









