
from django.shortcuts import render, redirect
from .forms import AlumnoForm, BusquedaAlumno, ProfesorFormulario
from .models import Alumno, Profesores
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def escuela(request):
    return render(request,'escuela.html')

def formulario_alumnos(request):
    if request.method == 'POST':
        formulario = AlumnoForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            alumno = Alumno(nombre=data['nombre'], apellido=data['apellido'])
            alumno.save()
            return render(request, 'indice/index.html', {'alumno': alumno})
          
    formulario = AlumnoForm()
    return render(request, 'escuela/formulario_alumnos.html', {'formulario': formulario})


def busqueda_alumno(request):
    alumnos_buscados = []
   
    dato = request.GET.get('busqueda_alumno', None)
      
    if dato is not None:
        alumnos_buscados = Alumno.objects.filter(nombre__icontains=dato)

    buscador = BusquedaAlumno()
    return render(request, "escuela/busqueda_alumno.html",

        {'buscador': buscador, 'alumnos_buscados': alumnos_buscados, 'dato': dato})

@login_required
def crear_profesor(request):
    
    if request.method == 'POST':
        form = ProfesorFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            profesor = Profesores(nombre=data['nombre'], apellido=data['apellido'], tarjeta_presentacion=data['tarjeta_presentacion'])
            profesor.save()
            return render(request, "indice/index.html", {})
            # return redirect('indice')
    
    form = ProfesorFormulario()
    return render(request, "escuela/crear_profesor.html", {'form': form})


def lista_profesores(request):
    lista_profesores = Profesores.objects.all()
    return render(
        request, "escuela/profesores_list.html",
        {'lista_profesores': lista_profesores}
    )


class ProfesorDetalle(DetailView):
    model = Profesores
    template_name = 'escuela/profesores_dato.html'
    
    
class ProfesorEditar(LoginRequiredMixin, UpdateView):
    model = Profesores
    success_url = '/escuela/profesores_list'
    template_name = 'escuela/profesores_form.html'
    fields = ['nombre', 'apellido', 'email', 'disciplina', 'tarjeta_presentacion']



class BorrarProfesor(LoginRequiredMixin,DeleteView):
    model = Profesores
    success_url = '/escuela/profesores_list'
    
