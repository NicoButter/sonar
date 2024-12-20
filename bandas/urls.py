from django.urls import path
from . import views

urlpatterns = [
    path('', views.banda_list, name='banda_list'),  # Lista de bandas
    path('create/', views.create_banda, name='create_banda'),  # Crear una banda
    path('<int:banda_id>/', views.banda_detail, name='banda_detail'),  # Detalle de una banda
    path('<int:banda_id>/edit/', views.edit_banda, name='edit_banda'),  # Editar una banda
]
