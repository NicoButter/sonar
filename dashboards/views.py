"""Vistas de la aplicación dashboards.

Contiene las vistas protegidas para los paneles de control
de representantes, administradores y moderadores.
"""

from django.shortcuts import render

from accounts.decorators import (
    admin_required,
    moderator_required,
    representative_required,
)


@representative_required
def representative_dashboard(request):
    """Muestra el dashboard del representante de banda.

    Requiere autenticación y rol de representante.
    Carga la banda asociada al usuario y la pasa al contexto.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        HttpResponse con el dashboard del representante.
    """
    banda = getattr(request.user, 'banda', None)
    context = {'banda': banda}
    return render(request, 'dashboards/representative_dashboard.html', context)


@admin_required
def admin_dashboard(request):
    """Muestra el dashboard del administrador.

    Requiere autenticación y rol de administrador.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        HttpResponse con el dashboard de admin.
    """
    return render(request, 'dashboards/admin_dashboard.html')


@moderator_required
def moderator_dashboard(request):
    """Muestra el dashboard del moderador.

    Requiere autenticación y rol de moderador.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        HttpResponse con el dashboard de moderador.
    """
    return render(request, 'dashboards/moderator_dashboard.html')
