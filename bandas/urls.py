from django.urls import path
from . import views

urlpatterns = [
    path('', views.banda_list, name='banda_list'),  # Lista de bandas
    path('create/', views.create_banda, name='create_banda'),  # Crear una banda
    path('bandas/eliminar/<int:banda_id>/', views.eliminar_banda, name='eliminar_banda'),
    path('editar_biografia/<int:banda_id>/', views.editar_biografia, name='edit_biografia'),
    path('editar_integrantes/<int:banda_id>/', views.editar_integrantes, name='edit_integrantes'),
    path('<int:banda_id>/', views.banda_detail, name='banda_detail'),  # Detalle de una banda
    path('<int:banda_id>/edit/', views.edit_banda, name='edit_banda'),  # Editar una banda
    path('bandas/<int:banda_id>/upload-imagen/', views.upload_imagen, name='upload_imagen'),
    path('eliminar-imagen/<int:imagen_id>/', views.eliminar_imagen, name='eliminar_imagen'),
    path('upload-demo/<int:banda_id>/', views.upload_demo, name='upload_demo')
]
