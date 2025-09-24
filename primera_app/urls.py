from django.urls import path, include
from rest_framework import routers
from primera_app import views

router = routers.DefaultRouter()

router.register(r'Nacionalidad', views.Nacionalidad_ViewSet)
router.register(r'Comuna', views.Comuna_ViewSet)
router.register(r'Autor', views.Autor_ViewSet)
router.register(r'Direccion', views.Direccion_ViewSet)
router.register(r'bibliotecas', views.BibliotecaViewSet)
router.register(r'lectores', views.LectorViewSet)
router.register(r'tipos-categorias', views.TipoCategoriaViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'libros', views.LibroViewSet)
router.register(r'prestamos', views.PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls))
]