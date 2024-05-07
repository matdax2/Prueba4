from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(max_length=100)

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    profesion = models.CharField(max_length=100)

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    FechaDeEntrega = models.DateField()
    entregado = models.BooleanField()