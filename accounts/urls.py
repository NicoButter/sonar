from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Página de aterrizaje
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # otras rutas de tu aplicación accounts
]
