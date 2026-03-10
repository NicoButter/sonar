"""Modelos de usuario personalizados para la aplicación accounts.

Define el modelo Usuario que extiende AbstractUser de Django,
agregando roles y campos de información adicional.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """Modelo de usuario personalizado con roles y datos adicionales.

    Extiende el modelo AbstractUser de Django para incluir campos
    de rol (admin, moderador, representante, visitante) e información
    de perfil como biografía y localidad.

    Attributes:
        is_admin: Indica si el usuario tiene rol de administrador.
        is_moderator: Indica si el usuario tiene rol de moderador.
        is_representative: Indica si el usuario es representante de banda.
        is_visitor: Indica si el usuario es visitante.
        bio: Texto libre con la biografía del usuario.
        localidad: Ciudad o localidad del usuario.
    """

    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_representative = models.BooleanField(default=False)
    is_visitor = models.BooleanField(default=False)

    bio = models.TextField(blank=True, null=True)
    localidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        """Retorna el nombre de usuario como representación en cadena."""
        return self.username
