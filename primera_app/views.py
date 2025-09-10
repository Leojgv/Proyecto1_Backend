from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Nacionalidad_Serializer, Comuna_Serializer, Autor_Serializer, Direccion_Serializer
from .models import Nacionalidad, Comuna, Autor, Direccion


# Create your views here.

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = Comuna_Serializer

class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = Nacionalidad_Serializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = Autor_Serializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = Direccion_Serializer