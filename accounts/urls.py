from django.urls import path
from .views import login_escuela, registrar, editar_usuario,usuario_datos
from django.contrib.auth.views import LogoutView

urlpatterns = [
	path ('login/', login_escuela, name='login'),
    path('editar/', editar_usuario, name='editar_usuario'),
    path('datos/', usuario_datos, name='usuario_datos'),
 	path ('registrar/', registrar, name='registrar'),
 	path ('logout/', LogoutView.as_view(template_name = 'accounts/logout.html'), name='logout')
 
 ]