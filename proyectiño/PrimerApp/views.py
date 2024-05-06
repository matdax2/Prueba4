from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

def inicio(request):
    return render(request, "PrimerApp/base.html")

def profesores(request):
    return render(request, "PrimerApp/profesores.html")

def estudiantes(request):
    return render(request, "PrimerApp/estudiantes.html")
