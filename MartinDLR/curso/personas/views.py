from django.http import HttpResponse
import datetime
from django.db import IntegrityError
from django.shortcuts import render

from prueba.models import Contactos

def principal(request):
  return render(request,'index.html')

def personas_ingresar(request):
  return render(request,'ingresar.html')

def personas_ingresar01(request):
    # Declaracion de lista
    mensajes = []
    mensaje =''
    tipo = 0
    if request.method == 'POST':
        try:
            #obtencion de datos desde el formulario

            nom = request.POST.get('nombre')
            ape = request.POST.get('apellido')
            cor = request.POST.get('correo')
            tel = request.POST.get('telefono')

            #Creacion de instancia de la clase Contacto, para uso de ORM
            nvo_contacto = Contactos(nombre=nom, apellido=ape, correo=cor, telefono=tel)
            #Guardar registro usando el formulario.
            nvo_contacto.save()
            #Emision de mensaje de ejecucion de solicitud
            #mensajes.append('Contacto ingresado con éxito')
            #Ahora vamos a cambiar MENSAJES por MENSAJE para que sea segun la naturaleza del mensaje
            mensaje = "El contacto fue almacenado con exito."
            tipo = 1
        except IntegrityError as e:
            #mensajes.append('Registro no se agrego pues correo ya existe')
            mensaje = "El contacto NO fue almacenado ."
            tipo = 2
            print(f"integrityError: {e}")
        #Enregar a la vista el mensaje.
        return render(request, 'ingresar.html',{'mensaje':mensaje, 'tipo':tipo})
    else:
        #Enregar a la vista el mensaje.
        return render(request, 'ingresar.html',{'mensaje':mensaje,'tipo':tipo})
        



def personas_consultar(request):
    return render(request, 'consultar.html')   

def personas_consultar01(request):
    mensaje =''
    tipo = 0
    nombre = '' 
    apellido = ''
    correo = ''
    telefono = ''
    if request.method == 'POST':
        try:
            cor = request.POST.get('correo')
            contacto = Contactos.objects.get(correo=cor)
            nombre   = contacto.nombre
            apellido = contacto.apellido
            correo   = contacto.correo  
            telefono = contacto.telefono
            mensaje = 'Consulta procesada con existo'
            tipo = 1
            return render(request, 'consultar01.html',{'mensaje':mensaje, 'tipo':tipo, 'nombre':nombre, 'apellido':apellido, 'correo':correo, 'telefono':telefono})
        except Contactos.DoesNotExist :
            mensaje = 'No hay registro del correo electronico' + cor
            tipo = 3
            return render(request, 'consultar.html',{'mensaje':mensaje, 'tipo':tipo})

def personas_borrar(request):
    
    mensaje =''
    tipo = 0
    try:
        datos = Contactos.objects.all() 
        mensaje = 'Consulta procesada con existo'
        tipo = 1
        return render(request, 'borrar.html',{'datos':datos, 'tipo':tipo, })
    except Except as e :
        mensaje = 'Ocurrio un error de lectura de datos' + str(e)
        tipo = 2
        return render(request, 'borrar.html',{'mensaje':mensaje, 'tipo':tipo})
   