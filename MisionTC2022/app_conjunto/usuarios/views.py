from http.client import HTTPResponse
from . import views
import json
from django.shortcuts import render
from .models import Tipo_Usuario
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest

# Create your views here.

def index(request):
    return HttpResponse("Hola MUNDO")

def newTipo_Usuario (request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            users = Tipo_Usuario(
                codigo_usuario = data["codigo_usuario"],
                tipo_usuario = data["tipo_usuario"]
            )
            users.save()
            return HttpResponse("Nuevo TIPO DE USUARIO agredado con Exito!")
        except:
            return HttpResponseBadRequest("Error en los datos envidos ABC")
    else:
        return HttpResponseNotAllowed(['POST'], 'METODO NO VALIDO')

def getTipo_Usuario(request):
    if request.method == 'GET':
        users = Tipo_Usuario.objects.all()
        if (not users):
            return HttpResponseBadRequest("No existe ese Tipo de Usuario en la base de datos")
        allUserData = []
        for x in users:
            data = {"Tipo_usuario" : x.tipo_usuario, "Codigo_Usuario" : x.codigo_usuario}
            allUserData.append(data)
        dataJson = json.dumps(allUserData)
        resp = HttpResponse()
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], 'METODO NO VALIDO') 
        
def getOneTipo_Usuario(request, codigo_usuario):
    if request.method == 'GET':
        user = Tipo_Usuario.objects.filter(codigo_usuario = codigo_usuario).first()
        if (not user):
            return HttpResponseBadRequest("No existe ese Tipo de Usuario con ese codigo")
        data = {"Tipo_usuario" : user.tipo_usuario, "Codigo_Usuario" : user.codigo_usuario}
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], 'METODO NO VALIDO') 





