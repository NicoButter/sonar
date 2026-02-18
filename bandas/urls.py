"""Configuración de URLs para la aplicación bandas.

Define las rutas para el listado, creación, edición, eliminación
de bandas, gestión de imágenes, demos, biografías e integrantes.
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.banda_list, name='banda_list'),
    path('create/', views.create_banda, name='create_banda'),
    path(
        'bandas/eliminar/<int:banda_id>/',
        views.eliminar_banda, name='eliminar_banda',
    ),
    path(
        'editar_biografia/<int:banda_id>/',
        views.editar_biografia, name='edit_biografia',
    ),
    path(
        'editar_integrantes/<int:banda_id>/',
        views.editar_integrantes, name='edit_integrantes',
    ),
    path('<int:banda_id>/', views.banda_detail, name='banda_detail'),
    path('<int:banda_id>/edit/', views.edit_banda, name='edit_banda'),
    path(
        'bandas/<int:banda_id>/upload-imagen/',
        views.upload_imagen, name='upload_imagen',
    ),
    path(
        'eliminar-imagen/<int:imagen_id>/',
        views.eliminar_imagen, name='eliminar_imagen',
    ),
    path(
        'upload-demo/<int:banda_id>/',
        views.upload_demo, name='upload_demo',
    ),
    path(
        'editar-imagen-representativa/<int:banda_id>/',
        views.actualizar_imagen_representativa,
        name='actualizar_imagen_representativa',
    ),
]
