"""
URL configuration for personas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path



#from personas.views import inicio1

from personas.views import principal
from personas.views import personas_ingresar
from personas.views import personas_ingresar01
from personas.views import personas_consultar
from personas.views import personas_consultar01
from personas.views import personas_borrar


urlpatterns = [
    path('admin/', admin.site.urls),
   
   
    
    path('', principal),
    path('personas_ingresar/', personas_ingresar),
    path('personas_ingresar01/', personas_ingresar01),
    path('personas_consultar/', personas_consultar),
    path('personas_consultar01/', personas_consultar01),
    path('personas_borrar/', personas_borrar),
    
]

# path('', inicio1),
