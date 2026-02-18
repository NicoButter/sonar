"""Configuración de la aplicación dashboards."""

from django.apps import AppConfig


class DashboardsConfig(AppConfig):
    """Clase de configuración para la aplicación dashboards.

    Attributes:
        default_auto_field: Tipo de campo auto-incremental por defecto.
        name: Nombre de la aplicación Django.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "dashboards"
