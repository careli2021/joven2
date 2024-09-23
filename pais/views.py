from django.shortcuts import render

# Create your views here.

from django.urls import path

from django.shortcuts import render
from webconfig.Query import SQL
def listar(request):
    odasql=SQL()
    listapais= odasql.listarJSON("exec uspListarPais")
    return render(request, "pais/pais.html",{
        "listapais":listapais
    })