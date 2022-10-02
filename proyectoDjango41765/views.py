from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template

def hola(request):
    return HttpResponse('<hi>Buenas Clase 41765!</hi>')

def fecha(request):
    fecha_y_hora=datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_y_hora}')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento aproxinada para tus {edad} años sería: {fecha}')

def mi_template(request):
    
    cargar_file = open(r'C:\Users\jor_p\04_Coder\Projects\Proyecto_Django_41765\templates\template.html','r')
    template = Template(cargar_file.read())
    cargar_file.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)