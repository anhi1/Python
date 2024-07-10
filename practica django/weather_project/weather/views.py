from django.shortcuts import render

from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("<h1>hola mundoo</h1>")


# es donde vamos a manejas la respuesta de una peticion, espera la respuesta y repsonde
