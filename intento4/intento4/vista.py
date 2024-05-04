from django.http import HttpResponse
from django.template import loader
import datetime

def mi_nombre(self, nombre):
    nombre = "Matias"
    texto = f"Mi nombre es: {nombre}"
    return HttpResponse(texto)

def probandoTemplate(self):
    nombre = "Matias"
    apellido = "Torterolo"
    notas = {1,2,3,4,5,6,7,8,9,10}
    diccionario = {"nombre":nombre, "apellido": apellido, "notas":notas}     
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)