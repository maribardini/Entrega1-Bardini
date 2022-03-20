   
from django import forms


class NivelInicialForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    
class PrimariaForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    
class SecundariaForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    
class BusquedaAlumno(forms.Form):
    busqueda_alumno = forms.CharField(label='Buscador',max_length=30)