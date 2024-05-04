from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):
    return HttpResponse("Hola Django - Coder")

def mi_nombre(self, nombre):
    texto = f"Mi nombre es: {nombre}"
    return HttpResponse(texto)


def probandoTemplate(self):
    nombre = "Matias"
    apellido = "Torterolo"
    notas = {1,2,3,4,5,6,7,8,9,10}
    diccionario = {"nombre":nombre, "apellido": apellido, "notas":notas}       
    miHtml = open("C:/Users/PC/Desktop/Prueba4/intento4/intento4/plantillas/template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    contexto = Context(diccionario)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)