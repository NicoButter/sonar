"""Decoradores de autorización para la aplicación accounts.

Proporciona decoradores reutilizables para verificar roles de usuario
(representante, administrador, moderador) en las vistas protegidas.
"""

from functools import wraps

from django.shortcuts import redirect


def role_required(role_attr, redirect_url='landing_page'):
    """Decorador genérico que verifica un atributo de rol en el usuario.

    Requiere que el usuario esté autenticado y tenga el atributo
    booleano indicado en ``True``. Si no cumple, redirige a la URL
    especificada.

    Args:
        role_attr: Nombre del atributo booleano del modelo Usuario
            (por ejemplo ``'is_representative'``).
        redirect_url: Nombre de la URL a la que redirigir si el usuario
            no tiene el rol. Por defecto ``'landing_page'``.

    Returns:
        Función decoradora que envuelve la vista.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if not getattr(request.user, role_attr, False):
                return redirect(redirect_url)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


def representative_required(view_func):
    """Decorador que verifica que el usuario sea representante.

    Combina la verificación de autenticación y el rol
    ``is_representative`` en un solo decorador.

    Args:
        view_func: Vista a proteger.

    Returns:
        Vista envuelta con la verificación de rol.
    """
    return role_required('is_representative')(view_func)


def admin_required(view_func):
    """Decorador que verifica que el usuario sea administrador.

    Combina la verificación de autenticación y el rol
    ``is_admin`` en un solo decorador.

    Args:
        view_func: Vista a proteger.

    Returns:
        Vista envuelta con la verificación de rol.
    """
    return role_required('is_admin')(view_func)


def moderator_required(view_func):
    """Decorador que verifica que el usuario sea moderador.

    Combina la verificación de autenticación y el rol
    ``is_moderator`` en un solo decorador.

    Args:
        view_func: Vista a proteger.

    Returns:
        Vista envuelta con la verificación de rol.
    """
    return role_required('is_moderator')(view_func)
