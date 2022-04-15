from django.urls import path
from .views import inicio, about, pages

urlpatterns = [
	path ('', inicio, name = 'inicio'),
 	path ('about', about, name = 'about'),
  	path ('pages', pages, name = 'pages')
 ]








