from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Página de aterrizaje
    path('login/', views.login_view, name='login'),       # Iniciar sesión
    path('logout/', views.logout_view, name='logout'),     # Cerrar sesión
    # otras rutas de tu aplicación accounts
]