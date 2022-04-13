from django.contrib import admin
from .models import Profesores, Alumno

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Profesores)

