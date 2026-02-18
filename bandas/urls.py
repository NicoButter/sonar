"""Configuración de URLs para la aplicación bandas.

Define las rutas para el listado, creación, edición, eliminación
de bandas, gestión de imágenes, demos, biografías e integrantes.
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.banda_list, name='banda_list'),
    path('crear/', views.create_banda, name='create_banda'),
    path('<int:banda_id>/', views.banda_detail, name='banda_detail'),
    path('<int:banda_id>/editar/', views.edit_banda, name='edit_banda'),
    path('<int:banda_id>/eliminar/', views.eliminar_banda, name='eliminar_banda'),
    path(
        '<int:banda_id>/editar-biografia/',
        views.editar_biografia, name='editar_biografia',
    ),
    path(
        '<int:banda_id>/editar-integrantes/',
        views.editar_integrantes, name='editar_integrantes',
    ),
    path(
        '<int:banda_id>/subir-imagen/',
        views.upload_imagen, name='upload_imagen',
    ),
    path(
        '<int:banda_id>/subir-demo/',
        views.upload_demo, name='upload_demo',
    ),
    path(
        '<int:banda_id>/editar-imagen-representativa/',
        views.actualizar_imagen_representativa,
        name='actualizar_imagen_representativa',
    ),
    path(
        'eliminar-imagen/<int:imagen_id>/',
        views.eliminar_imagen, name='eliminar_imagen',
    ),
    path(
        '<int:banda_id>/descargar/',
        views.descargar_demo, name='descargar_demo',
    ),
]
