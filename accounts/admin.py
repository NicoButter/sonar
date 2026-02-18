"""Configuración del panel de administración para la aplicación accounts.

Registra el modelo Usuario con una interfaz de administración
personalizada que incluye campos de rol e información de perfil.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


class UsuarioAdmin(UserAdmin):
    """Configuración personalizada del admin para el modelo Usuario.

    Extiende UserAdmin para mostrar y gestionar los campos
    adicionales de roles (admin, moderador, representante, visitante)
    y la información de perfil (bio, localidad).

    Attributes:
        list_display: Campos visibles en la lista de usuarios.
        list_filter: Filtros disponibles en la barra lateral.
        fieldsets: Agrupación de campos en el formulario de edición.
        add_fieldsets: Campos del formulario de creación de usuario.
        search_fields: Campos habilitados para búsqueda.
        ordering: Orden predeterminado de la lista.
    """

    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'is_admin', 'is_moderator', 'is_representative', 'is_visitor',
        'bio', 'localidad', 'is_active', 'date_joined',
    )

    list_filter = (
        'is_admin', 'is_moderator', 'is_representative',
        'is_visitor', 'is_active',
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {
            'fields': ('first_name', 'last_name', 'bio', 'localidad'),
        }),
        ('Permisos', {
            'fields': (
                'is_active', 'is_admin', 'is_moderator',
                'is_representative', 'is_visitor',
            ),
        }),
        ('Fechas', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password1', 'password2',
                'first_name', 'last_name', 'bio', 'localidad',
                'is_admin', 'is_moderator', 'is_representative',
                'is_visitor',
            ),
        }),
    )

    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)


admin.site.register(Usuario, UsuarioAdmin)
