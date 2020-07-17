from django.shortcuts import render,HttpResponse
from django.template import loader
from portafolio.models import Proyecto

# Create your views here.
def portafolio(request):
    publicaciones = Proyecto.objects.all()
    return render(request,"portafolio.html",{"publicaciones":publicaciones})