from django.urls import path, include
from rest_framework import routers
from primera_app import views

router = routers.DefaultRouter()

router.register(r'Nacionalidad', views.NacionalidadViewSet)
router.register(r'Comuna', views.ComunaViewSet)
router.register(r'Autor', views.AutorViewSet)
router.register(r'Direccion', views.DireccionViewSet)
router.register(r'bibliotecas', views.BibliotecaViewSet)
router.register(r'lectores', views.LectorViewSet)
router.register(r'tipos-categorias', views.TipoCategoriaViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'libros', views.LibroViewSet)
router.register(r'prestamos', views.PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls))
]