from django.urls import path
from PrimerApp import views

urlpatterns = [
    path('', views.inicio, name="Principal"),
    path('formulario/', views.cursoFormulario, name="Formulario de cursos"),
    path('profForms/', views.profFormulario, name="Formulario de profesores"),
    path('estform/', views.estFormulario, name="Formulario de estudiantes"),
    path('busqueda/', views.busqueda, name="busqueda"),
    path('buscar/', views.buscar, name="Buscador"),
    path('gerardo/', views.Geralt_De_Rivia, name="gerardito"),
]
