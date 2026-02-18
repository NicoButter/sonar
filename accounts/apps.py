"""Configuración de la aplicación accounts."""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Clase de configuración para la aplicación accounts.

    Attributes:
        default_auto_field: Tipo de campo auto-incremental por defecto.
        name: Nombre de la aplicación Django.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
