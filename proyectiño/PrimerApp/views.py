from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from PrimerApp.forms import *

def inicio(request):
    return render(request, "PrimerApp/base.html")

def cursoFormulario(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            curso = Curso(nombre = informacion["curso"], camada = informacion["camada"])
            curso.save()
            return render(request, "PrimerApp/base.html")
    else:
        formulario = CursoFormulario()
    return render(request, "PrimerApp/cursoFormulario.html", {"formulario": formulario})

def profFormulario(request):
    if request.method == "POST":
        prof_formulario = ProfeFormulario(request.POST)
        print(prof_formulario)
        if prof_formulario.is_valid:
            informacion = prof_formulario.cleaned_data
            profesor = Profesor(nombre = informacion["nombre"], apellido = informacion["apellido"], email = informacion["email"], profesion = informacion["profesion"])
            profesor.save()
            return render(request, "PrimerApp/base.html")
    else:
        prof_formulario = ProfeFormulario()
    return render(request, "PrimerApp/profeFormulario.html", {"prof_formulario": prof_formulario})

def estFormulario(request):
    if request.method == "POST":
        est_formulario = EstFormulario(request.POST)
        print(est_formulario)
        if est_formulario.is_valid:
            informacion = est_formulario.cleaned_data
            estudiante = Estudiante(nombre = informacion["nombre"], apellido = informacion["apellido"], email = informacion["email"], edad = informacion["edad"])
            estudiante.save()
            return render(request, "PrimerApp/base.html")
    else:
        est_formulario = EstFormulario()
    return render(request, "PrimerApp/estFormulario.html", {"est_formulario": est_formulario})

def busqueda(request):
    return render(request, "PrimerApp/buscador.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "PrimerApp/busqueda.html", {"cursos":cursos, "camada": camada})
    else:
        respuesta = "No enviastes datos"
    return HttpResponse(respuesta)

def Geralt_De_Rivia(request):
    return render(request, "PrimerApp/Gerardo.html")