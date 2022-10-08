from django.db import models

# Create your models here.


class TipoUsuario(models.Model):
    idTipoUsuario = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=255, blank=True)

""" class TipoUsuario(models.Models):
    idTipoUsuario = models.IntegerField(primary_key=True)
    tipoUsuario = models.CharField(max_length=255) """
    

class Persona(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    correo = models.CharField(max_length=200, blank=False)
    clave = models.CharField(max_length=200, blank=False)
    telefono = models.CharField(max_length=12)
    idPersona = models.AutoField(primary_key=True)
    TipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    

    
    