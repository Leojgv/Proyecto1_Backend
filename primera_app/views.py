from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Nacionalidad_Serializer, Comuna_Serializer, Autor_Serializer, Direccion_Serializer
from .models import Nacionalidad, Comuna, Autor, Direccion

def home(request):
    return render(request, 'index.html')


# Create your views here.

class Comuna_ViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = Comuna_Serializer

class Nacionalidad_ViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = Nacionalidad_Serializer

class Autor_ViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = Autor_Serializer

class Direccion_ViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = Direccion_Serializer