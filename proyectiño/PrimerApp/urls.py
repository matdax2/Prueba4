from django.urls import path
from PrimerApp import views

urlpatterns = [
    path('', views.inicio, name="Principal"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
]
