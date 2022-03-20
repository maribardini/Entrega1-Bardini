from django.http import HttpResponse
import random
from django.shortcuts import render
from .forms import NivelInicialForm, PrimariaForm, SecundariaForm, BusquedaAlumno
from .models import Nivel_Inicial, Primaria, Secundaria
from django.template import loader

# Create your views here.
def escuela(request):
    return render(request,'escuela.html')

def formulario_nivel_inicial(request):
    if request.method == 'POST':
        formulario = NivelInicialForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            alumno = Nivel_Inicial(nombre=data['nombre'], apellido=data['apellido'])
            alumno.save()
            return render(request, 'indice/index.html', {'alumno': alumno})
          
    formulario = NivelInicialForm()
    return render(request, 'escuela/nivel_inicial.html', {'formulario': formulario})


def formulario_primaria(request):
    if request.method == 'POST':
        formulario = PrimariaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            alumno = Primaria(nombre=data['nombre'], apellido=data['apellido'])
            alumno.save()
            return render(request, 'indice/index.html', {'alumno': alumno})
          
    formulario = PrimariaForm()
    return render(request, 'escuela/primaria.html', {'formulario': formulario})


def formulario_secundaria(request):
    if request.method == 'POST':
        formulario = SecundariaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            alumno = Secundaria(nombre=data['nombre'], apellido=data['apellido'])
            alumno.save()
            return render(request, 'indice/index.html', {'alumno': alumno})
          
    formulario = SecundariaForm()
    return render(request, 'escuela/secundaria.html', {'formulario': formulario})

def busqueda_alumno(request):
    alumnos_buscados = []
   
    dato = request.GET.get('busqueda_alumno', None)
      
    if dato is not None:
        alumnos_buscados = [list(Nivel_Inicial.objects.filter(nombre__icontains=dato)),
        list(Nivel_Inicial.objects.filter(apellido__icontains=dato)), 
        list(Primaria.objects.filter(nombre__icontains=dato)),
        list(Primaria.objects.filter(apellido__icontains=dato)),
        list(Secundaria.objects.filter(nombre__icontains=dato)),
        list(Secundaria.objects.filter(apellido__icontains=dato))]

    buscador = BusquedaAlumno()
    return render(request, "escuela/busqueda_alumno.html",

        {'buscador': buscador, 'alumnos_buscados': alumnos_buscados, 'dato': dato})
   
