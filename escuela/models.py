from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Profesores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    disciplina = models.CharField(max_length=30,null=True)
    foto = models.ImageField(upload_to='avatar',blank=True, null=True)
    tarjeta_presentacion = RichTextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__ (self):
        return f'{self.nombre} {self.apellido}'


