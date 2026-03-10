"""Configuración de URLs para la aplicación accounts.

Define las rutas para la página de aterrizaje, inicio de sesión
y cierre de sesión.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]