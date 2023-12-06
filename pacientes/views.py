from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
# importar model Soldado
from .models import Soldado

# Create your views here.

def index(request):
    return render(request, 'helloworld.html')

def soldado(request, codigo_soldado):
    print(codigo_soldado)
    #crear objeto json
    soldado = get_object_or_404(Soldado, codigo_soldado=codigo_soldado)
 
    return JsonResponse({
            'id': soldado.id,
            'codigo_soldado': soldado.codigo_soldado,
            'nombre': soldado.nombre,
            'rango': soldado.rango,
            'fecha_nacimiento': str(soldado.fecha_nacimiento),
            'fecha_ingreso': str(soldado.fecha_ingreso),
            'unidad': soldado.unidad,
            'especialidad': soldado.especialidad,
            'grupo_sanguineo': soldado.grupo_sanguineo,
            'alergias': soldado.alergias,
            'condiciones_medicas': soldado.condiciones_medicas,
        })