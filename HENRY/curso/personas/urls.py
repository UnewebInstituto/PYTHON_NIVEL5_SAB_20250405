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

from personas.views import principal
from personas.views import personas_ingresar
from personas.views import personas_ingresar01
from personas.views import personas_consultar
from personas.views import personas_consultar01
from personas.views import personas_borrar
from personas.views import personas_borrar01
from personas.views import personas_actualizar
from personas.views import personas_actualizar01
from personas.views import personas_actualizar02
from personas.views import personas_reporte
from personas.views import personas_reporte_json
from personas.views import personas_reporte_xml
from personas.views import personas_procesa_json

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal),
    path('personas_ingresar/', personas_ingresar),
    path('personas_ingresar01/', personas_ingresar01),
    path('personas_consultar/', personas_consultar),
    path('personas_consultar01/', personas_consultar01),
    path('personas_borrar/', personas_borrar),
    path('personas_borrar01/', personas_borrar01),
    path('personas_actualizar/', personas_actualizar),
    path('personas_actualizar01/', personas_actualizar01),
    path('personas_actualizar02/', personas_actualizar02),
    path('personas_reporte/', personas_reporte),
    path('personas_api_json/', personas_reporte_json),
    path('personas_api_xml/', personas_reporte_xml),
    path('personas_procesa_json/', personas_procesa_json),
]
