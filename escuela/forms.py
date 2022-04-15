   
from traceback import format_stack
from django import forms
from ckeditor.fields import RichTextFormField
from django.utils import timezone


class AlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    
    
class BusquedaAlumno(forms.Form):
    busqueda_alumno = forms.CharField(label='Buscador',max_length=30)
    
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()    
    disciplina = forms.CharField(max_length=30)
    tarjeta_presentacion = RichTextFormField(required=False)
