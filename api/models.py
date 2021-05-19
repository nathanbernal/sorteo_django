from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    usuarioId = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=200)
    paterno = models.CharField(max_length=200)
    materno = models.CharField(max_length=100)
    email = models.CharField(max_length=500, blank=False, null=True)
    contrasena = models.CharField(max_length=100, null=True)
    registro_fecha = models.DateTimeField(default=timezone.now)
    activo = models.IntegerField(default=0)

    def __str__(self):
        return self.title
