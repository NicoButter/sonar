"""Vistas de la aplicación accounts.

Contiene las vistas para la página de aterrizaje, inicio de sesión
y cierre de sesión de los usuarios.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def landing_page(request):
    """Renderiza la página de aterrizaje principal del sitio.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        HttpResponse con el template de la landing page.
    """
    return render(request, 'landing_page.html')


def login_view(request):
    """Procesa el inicio de sesión del usuario.

    Si el método es POST, autentica las credenciales y redirige al
    dashboard correspondiente según el rol del usuario. Si la
    autenticación falla, muestra un mensaje de error.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        HttpResponse con redirección al dashboard o al formulario
        de login con mensaje de error.
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_representative:
                return redirect(reverse('representative_dashboard'))
            elif user.is_admin:
                return redirect(reverse('admin_dashboard'))
            elif user.is_moderator:
                return redirect(reverse('moderator_dashboard'))
            else:
                return redirect('landing_page')

        else:
            return render(
                request, 'login.html',
                {'error': 'Nombre de usuario o contraseña incorrectos.'}
            )
    return render(request, 'login.html')


def logout_view(request):
    """Cierra la sesión del usuario y redirige a la landing page.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        HttpResponseRedirect hacia la página de aterrizaje.
    """
    logout(request)
    return redirect('landing_page')
