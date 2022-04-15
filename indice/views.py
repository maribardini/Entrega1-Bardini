
from django.shortcuts import render, redirect


# Create your views here.
def inicio (request):
    return render(request, "indice/index.html", {})

def about (request):
    return render(request, "indice/about.html", {})

def pages (request):
    return render(request, "indice/pages.html", {})


