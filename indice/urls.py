from django.urls import path
from .views import inicio, login_escuela, registrar, editar
from django.contrib.auth.views import LogoutView

urlpatterns = [
	path ('', inicio, name = 'inicio'),
	path ('login/', login_escuela, name='login'),
 	path ('registrar/', registrar, name='registrar'),
  	path ('editar/', editar, name='editar'),
 	path ('logout/', LogoutView.as_view(template_name = 'indice/logout.html'), name='logout')
 
 ]








