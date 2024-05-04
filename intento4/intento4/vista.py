from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def mi_nombre(self, nombre):
    texto = f"Mi nombre es: {nombre}"
    return HttpResponse(texto)
