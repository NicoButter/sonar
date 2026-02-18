"""Vistas de la aplicación dashboards.

Contiene las vistas protegidas para los paneles de control
de representantes, administradores y moderadores.
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.models import Usuario  # noqa: F401


@login_required
def representative_dashboard(request):
    """Muestra el dashboard del representante de banda.

    Verifica que el usuario tenga el rol de representante.
    Carga la banda asociada al usuario y la pasa al contexto.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        HttpResponse con el dashboard del representante o
        redirección a la landing page si no tiene el rol.
    """
    if not request.user.is_representative:
        return redirect('landing_page')

    banda = getattr(request.user, 'banda', None)
    context = {'banda': banda}
    return render(request, 'representative_dashboard.html', context)


@login_required
def admin_dashboard(request):
    """Muestra el dashboard del administrador.

    Verifica que el usuario tenga el rol de administrador.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        HttpResponse con el dashboard de admin o redirección
        a la landing page si no tiene el rol.
    """
    if not request.user.is_admin:
        return redirect('landing_page')

    return render(request, 'dashboard/admin_dashboard.html')


@login_required
def moderator_dashboard(request):
    """Muestra el dashboard del moderador.

    Verifica que el usuario tenga el rol de moderador.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        HttpResponse con el dashboard de moderador o redirección
        a la landing page si no tiene el rol.
    """
    if not request.user.is_moderator:
        return redirect('landing_page')

    return render(request, 'dashboard/moderator_dashboard.html')
