from rest_framework import serializers
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, TipoCategoria, Categoria, Libro, Prestamo


class Nacionalidad_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = '__all__'

class Autor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class Comuna_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

class Direccion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = '__all__'

class LectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lector
        fields = '__all__'

class TipoCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCategoria
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'