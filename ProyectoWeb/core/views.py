from django.shortcuts import render,HttpResponse
from django.template import loader
# Create your views here.

def inicio(request):  
    return render(request,"inicio.html")

def contacto(request):
    return render(request,"contacto.html")


