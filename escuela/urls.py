from django.urls import path
from .views import escuela, formulario_nivel_inicial, formulario_primaria, formulario_secundaria, busqueda_alumno

urlpatterns = [
	path ('escuela/', escuela, name = 'escuela'),
    path('nivel-inicial/', formulario_nivel_inicial, name='formulario_nivel_inicial'),
    path('primaria/', formulario_primaria, name='formulario_primaria'),
    path('secundaria/', formulario_secundaria, name='formulario_secundaria'),
    path('busqueda-alumno/', busqueda_alumno, name="busqueda_alumno")
 ]