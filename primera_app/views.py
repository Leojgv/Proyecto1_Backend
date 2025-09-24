from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Nacionalidad_Serializer, Comuna_Serializer, Autor_Serializer, Direccion_Serializer, BibliotecaSerializer, LectorSerializer, TipoCategoriaSerializer, CategoriaSerializer, LibroSerializer, PrestamoSerializer
from .models import Nacionalidad, Comuna, Autor, Direccion, Biblioteca, Lector, TipoCategoria, Categoria, Libro, Prestamo

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

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer

class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer

class TipoCategoriaViewSet(viewsets.ModelViewSet):
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer