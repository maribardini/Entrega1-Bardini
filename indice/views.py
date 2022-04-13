
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import MiCreacionUser, MiEdicionUser
from django.contrib.auth.decorators import login_required
from .models import Avatar


# Create your views here.
def inicio (request):
    return render(request, "indice/index.html", {})


def login_escuela (request):    
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request,user)
                return render(request,'indice/index.html', {'msj':'Te logueaste'})
            else:
                return render(request, 'indice/login.html', {'form': form, 'msj': 'El usuario no se pudo autenticar'})
        else:
           return render(request, 'indice/login.html', {'form': form, 'msj': 'El formulario no es válido'} )
    else:   
        form = AuthenticationForm()
        return render(request,'indice/login.html',{'form':form, 'msj': ''})
    
def registrar (request):
    
    if request.method == 'POST':
        form = MiCreacionUser(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data ['username']
            form.save()
            return render (request, 'indice/index.html', {'msj': f'Se creó el usuario {username}'})
        else:
            return render(request,'indice/registrar.html', {'form':form, 'msj': ''})    
        
    
    form = MiCreacionUser()
    return render(request,'indice/registrar.html', {'form':form, 'msj': ''})

@login_required
def editar(request):
    msj = ''
    
    if request.method == 'POST':
        form = MiEdicionUser(request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            logued_user = request.user
            logued_user.email = data.get('email')
            logued_user.first_name = data.get('first_name', '')
            logued_user.last_name = data.get('last_name')

            if data.get('password1') == data.get('password2') and len(data.get('password1')) > 8:
                logued_user.set_password(data.get('password1'))
            else:
                msj= 'No se modificó la contraseña'
                
            logued_user.save()
            
            return render(request, 'indice/index.html', {'msj': msj, 'user_avatar_url': buscar_url_avatar(request.user)})
        else:
            return render(request, 'indice/editar_user.html', {'form': form, 'msj': '', 'user_avatar_url': buscar_url_avatar(request.user)})
        
    
    form = MiEdicionUser(
        initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'username': request.user.username
        }
    )
    
    return render(request, 'indice/editar_user.html', {'form': form, 'msj': '', 'user_avatar_url': buscar_url_avatar(request.user)})


def buscar_url_avatar(user):
    return Avatar.objects.filter(user=user)[0].imagen.url
     
    