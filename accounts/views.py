from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import MiCreacionUser, EditFullUser
from django.contrib.auth.decorators import login_required
from .models import UserExtension

# Create your views here.
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
                return render(request, 'accounts/login.html', {'form': form, 'msj': 'El usuario no se pudo autenticar'})
        else:
           return render(request, 'accounts/login.html', {'form': form, 'msj': 'El formulario no es válido'} )
    else:   
        form = AuthenticationForm()
        return render(request,'accounts/login.html',{'form':form, 'msj': ''})
    
def registrar (request):
    
    if request.method == 'POST':
        form = MiCreacionUser(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data ['username']
            form.save()
            return render (request, 'indice/index.html', {'msj': f'Se creó el usuario {username}'})
        else:
            return render(request,'accounts/registrar.html', {'form':form, 'msj': 'El formulario no es válido'})    
        
    
    form = MiCreacionUser()
    return render(request,'accounts/registrar.html', {'form':form})


@login_required
def editar_usuario(request):
    
    user_extension_logued, _ = UserExtension.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = EditFullUser(request.POST, request.FILES)
        
        if form.is_valid():
            
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            user_extension_logued.avatar = form.cleaned_data['avatar']
            user_extension_logued.link = form.cleaned_data['link']
            user_extension_logued.more_description = form.cleaned_data['more_description']
            
            if form.cleaned_data['password1'] != '' and form.cleaned_data['password1'] == form.cleaned_data['password2']:
                request.user.set_password(form.cleaned_data['password1'])
            
            request.user.save()
            user_extension_logued.save()
            
            return redirect('inicio')
        else:
            return render(request, 'accounts/editar_usuario.html', {'form': form, 'msj': 'El formulario no es valido.'})
            
    
    form = EditFullUser(
        initial={
            'email': request.user.email,
            'password1': '',
            'password2': '',
            'first_name': request.user.first_name,
            'last_name': request.user.last_name, 
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
            'more_description': user_extension_logued.more_description
        }
    )
    return render(request, 'accounts/editar_user.html', {'form': form})

@login_required
def usuario_datos(request):
    return render(request, 'accounts/usuario_datos.html', {})
     
    