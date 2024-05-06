from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada="19881")
    curso.save()
    texto = f"Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)

