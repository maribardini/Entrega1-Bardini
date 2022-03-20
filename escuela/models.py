from django.db import models


class Nivel_Inicial(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)

    def __str__(self): 
        return f'{self.nombre} {self.apellido}'

class Primaria(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)

    def __str__ (self): 
        return f'{self.nombre} {self.apellido}'

class Secundaria(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)

    def __str__ (self): 
        return f'{self.nombre} {self.apellido}'