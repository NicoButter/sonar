"""Configuración de la aplicación bandas."""

from django.apps import AppConfig


class BandasConfig(AppConfig):
    """Clase de configuración para la aplicación bandas.

    Attributes:
        default_auto_field: Tipo de campo auto-incremental por defecto.
        name: Nombre de la aplicación Django.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "bandas"
