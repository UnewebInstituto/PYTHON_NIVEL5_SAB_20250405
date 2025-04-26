from django.http import HttpResponse
import datetime
from django.shortcuts import render

from django.db import IntegrityError
# Declaración del modelo Contactos
from prueba.models import Contactos
#json
from django.http import JsonResponse
#xml
import xml.etree.ElementTree as ET

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

def personas_borrar01(request):
  mensaje = ''
  tipo = 0
  if request.method == 'GET':
    try:
      idTmp = request.GET.get('id')
      Contactos.objects.filter(id=idTmp).delete()
      mensaje = 'Contacto fue eliminado con éxito.'
      tipo = 1
    except Exception as e:
      mensaje = 'Ocurrió un error al procesar la consulta: ' + str(e)
      tipo = 2
    # Recargar los datos de la consulta a Contactos
    datos = Contactos.objects.all() 
    # Devolver el resultado de la consulta
    return render(request, 'borrar.html', {'datos': datos, 'mensaje': mensaje, 'tipo': tipo})

def personas_actualizar(request):
  mensaje = ''
  tipo = 0
  try:
    datos = Contactos.objects.all() 
    mensaje = 'Consulta procesada con éxito'
    tipo = 1
    return render(request, 'actualizar.html',{'datos':datos,'tipo':tipo})
  except Exception as e:
    mensaje = 'Ocurrió un error al procesar la consulta: ' + str(e)
    tipo = 2
    return render(request, 'actualizar.html', {'mensaje': mensaje, 'tipo': tipo})

def personas_actualizar01(request):
  mensaje = ''
  tipo = 0
  idTmp = 0
  nombre = ''
  apellido = ''
  correo = ''
  telefono = ''
  if request.method == 'GET':
    try:
      idTmp = request.GET.get('id')
      contacto = Contactos.objects.get(id=idTmp)
      nombre = contacto.nombre
      apellido = contacto.apellido
      correo = contacto.correo
      telefono = contacto.telefono
      mensaje = 'Consulta procesada con éxito. Proceda con la modificación del registro.'
      tipo = 1
      return render(request, 'actualizar01.html',{'mensaje':mensaje,'tipo':tipo, 'idTmp':idTmp, 'nombre':nombre, 'apellido':apellido, 'correo':correo, 'telefono':telefono})
    except Contactos.DoesNotExist:
      mensaje = 'No se tienen datos almacenados para actualizar. ' + cor
      tipo = 3 
      return render(request, 'actualizar01.html',{'mensaje':mensaje,'tipo':tipo})

def personas_actualizar02(request):
  mensaje = ''
  tipo = 0
  idTmp = 0
  nombreTmp = ''
  apellidoTmp = ''
  correoTmp = ''
  telefonoTmp = ''
  if request.method == 'POST':
    try:
      idTmp = request.POST.get('id')
      nombreTmp = request.POST.get('nombre')
      apellidoTmp = request.POST.get('apellido')
      correoTmp = request.POST.get('correo')
      telefonoTmp = request.POST.get('telefono')
      Contactos.objects.filter(id=idTmp).update(nombre=nombreTmp, apellido=apellidoTmp, telefono=telefonoTmp)
      mensaje = 'Contacto fue actualizado con éxito.'
      tipo = 1
    except Exception as e:
      mensaje = 'Ocurrió un error al procesar la consulta: ' + str(e)
      tipo = 2
    # Recargar los datos de la consulta a Contactos
    datos = Contactos.objects.all() 
    # Devolver el resultado de la consulta
    return render(request, 'actualizar.html', {'datos': datos, 'mensaje': mensaje, 'tipo': tipo})


def personas_reporte(request):
  mensaje = ''
  tipo = 0
  try:
    datos = Contactos.objects.all() 
    mensaje = 'Consulta procesada con éxito'
    tipo = 1
    return render(request, 'reporte.html',{'datos':datos,'tipo':tipo})
  except Exception as e:
    mensaje = 'Ocurrió un error al procesar la consulta: ' + str(e)
    tipo = 2
    return render(request, 'reporte.html', {'mensaje': mensaje, 'tipo': tipo})

def personas_reporte_json(request):
    mensaje = ''
    tipo = 0
    try:
        datos = list(Contactos.objects.values())  # Convertir a lista de diccionarios
        mensaje = 'Consulta procesada con éxito'
        tipo = 1
        response_data = {
            'tipo': tipo,
            'mensaje': mensaje,
            'datos': datos
        }
        return JsonResponse(response_data)  # Retornar respuesta en formato JSON
    except Exception as e:
        mensaje = 'Ocurrió un error al procesar la consulta: ' + str(e)
        tipo = 2
        response_data = {
            'tipo': tipo,
            'mensaje': mensaje
        }
        return JsonResponse(response_data, status=500)  # Retornar error en formato JSON

def personas_reporte_xml(request):
  mensaje = ''
  tipo = 0
  try:
      datos = list(Contactos.objects.values())  # Convertir a lista de diccionarios
      mensaje = 'Consulta procesada con éxito'
      tipo = 1
      
      # Crear el elemento raíz
      root = ET.Element("response")
      
      # Agregar tipo y mensaje
      ET.SubElement(root, "tipo").text = str(tipo)
      ET.SubElement(root, "mensaje").text = mensaje
      
      # Agregar datos de contactos
      contactos_element = ET.SubElement(root, "contactos")
      for dato in datos:
          contacto_element = ET.SubElement(contactos_element, "contacto")
          ET.SubElement(contacto_element, "id").text = str(dato['id'])
          ET.SubElement(contacto_element, "nombre").text = dato['nombre']
          ET.SubElement(contacto_element, "apellido").text = dato['apellido']
          ET.SubElement(contacto_element, "telefono").text = dato['telefono']
          ET.SubElement(contacto_element, "correo").text = dato['correo']
      
      # Convertir el árbol XML a una cadena
      xml_str = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
      
      return HttpResponse(xml_str, content_type='application/xml')  # Retornar respuesta en formato XML
  except Exception as e:
      mensaje = 'Ocurrió un error al procesar la consulta: ' + str(e)
      tipo = 2
      
      # Crear el elemento raíz para el error
      root = ET.Element("response")
      ET.SubElement(root, "tipo").text = str(tipo)
      ET.SubElement(root, "mensaje").text = mensaje
      
      xml_str = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
      
      return HttpResponse(xml_str, content_type='application/xml', status=500)  # Retornar error en formato XML

def personas_procesa_json(request):
  mensaje = ''
  tipo = ''
  return render(request, 'reporte_json.html', {'mensaje': mensaje, 'tipo': tipo})