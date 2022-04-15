from django.urls import path
from .views import inicio, about

urlpatterns = [
	path ('', inicio, name = 'inicio'),
 	path ('about', about, name = 'about')
 ]








