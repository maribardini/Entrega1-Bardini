from django.urls import path
from .views import escuela, formulario_alumnos, busqueda_alumno, ProfesorDetalle, ProfesorEditar, BorrarProfesor,crear_profesor, lista_profesores

urlpatterns = [
	path ('escuela/', escuela, name = 'escuela'),
    path('alumnos/', formulario_alumnos, name='formulario_alumnos'),
    path('busqueda-alumno/', busqueda_alumno, name="busqueda_alumno"),
    
    path('profesores/', lista_profesores, name="profesores"),
    path('profesores/crear/',crear_profesor, name="crear_profesor"),
    path('profesores/<int:pk>/', ProfesorDetalle.as_view(), name="profesores_detalle"),
    path('profesores/<int:pk>/editar/', ProfesorEditar.as_view(), name="profesores_editar"),
    path('profesores/<int:pk>/borrar/', BorrarProfesor.as_view(), name="profesores_borrar")
    
    ]