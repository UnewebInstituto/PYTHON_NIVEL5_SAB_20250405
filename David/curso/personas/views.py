from django.http import HttpResponse
import datetime
from django.shortcuts import render

from django.db import IntegrityError
# Declaración del modelo Contactos
from prueba.models import Contactos

def principal(request):
  return render(request,'index.html')

def personas_ingresar(request):
  return render(request,'ingresar.html')

def personas_ingresar01(request):
    mensaje = ''
    tipo = 0
    if request.method == 'POST':
        try:
            # Obtención de datos desde el formulario
            nom = request.POST.get('nombre')
            ape = request.POST.get('apellido')
            cor = request.POST.get('correo')
            tel = request.POST.get('telefono')
            # Creación de instancia de la clase Contactos para uso de ORM
            nvo_contacto = Contactos(nombre=nom, apellido=ape, correo=cor, telefono=tel)
            # Guardar registro ingresado a través del formulario
            nvo_contacto.save()
            # Emitir mensaje de ejecución
            mensaje = "El contacto fue almacenado con éxito."
            tipo = 1
        except IntegrityError as e:
            mensaje = "El contacto no fue almacenado por error de integridad de datos."
            tipo = 2
            print(f"IntegrityError: {e}")
        # Devolver a la vista el mensaje
        return render(request, 'ingresar.html',{'mensaje':mensaje,'tipo':tipo})
    else:
        return render(request, 'ingresar.html',{'mensaje':mensaje,'tipo':tipo})

def personas_consultar(request):
  return render(request,'consultar.html')

def personas_consultar01(request):
  mensaje = ''
  tipo = 0
  nombre = ''
  apellido = ''
  correo = ''
  telefono = ''
  try:
    cor = request.POST.get('correo')
    contacto = Contactos.objects.get(correo=cor)
    nombre = contacto.nombre
    apellido = contacto.apellido
    correo = contacto.correo
    telefono = contacto.telefono
    mensaje = 'Consulta procesada con éxito'
    tipo = 1
    return render(request, 'consultar01.html',{'mensaje':mensaje,'tipo':tipo, 'nombre':nombre, 'apellido':apellido, 'correo':correo, 'telefono':telefono})
  except Contactos.DoesNotExist:
    mensaje = 'No se tienen datos almacenados para el correo electrónico ' + cor
    tipo = 3 
    return render(request, 'consultar.html',{'mensaje':mensaje,'tipo':tipo})

def personas_borrar(request):
    mensaje = ''
    tipo = 0
    try:
      datos = Contactos.objects.all() 
      mensaje = 'Consulta procesada con éxito'
      tipo = 1
      return render(request, 'borrar.html',{'datos':datos,'tipo':tipo})
    except Exception as e:
      mensaje = 'Ocurrió un error al procesar la consulta: ' + str(e)
      tipo = 2
      return render(request, 'borrar.html', {'mensaje': mensaje, 'tipo': tipo})