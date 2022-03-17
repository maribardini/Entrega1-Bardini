from django.http import HttpResponse
import random
from django.shortcuts import render

from django.template import loader

# Create your views here.
def inicio(request):
    return render(request,'indice/index.html',{})