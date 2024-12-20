from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Definir un modelo de formulario personalizado si es necesario
class UsuarioAdmin(UserAdmin):
    # Definir los campos que se mostrarán en la lista de usuarios
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_admin', 'is_moderator', 'is_representative', 'is_visitor', 'bio', 'localidad', 'is_active', 'date_joined')
    
    # Añadir filtros a la vista de lista de usuarios
    list_filter = ('is_admin', 'is_moderator', 'is_representative', 'is_visitor', 'is_active')

    # Campos que aparecerán en la vista de detalles del usuario
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'bio', 'localidad')}),
        ('Permisos', {'fields': ('is_active', 'is_admin', 'is_moderator', 'is_representative', 'is_visitor')}),
        ('Fechas', {'fields': ('last_login', 'date_joined')}),
    )

    # Campos que estarán disponibles para editar en el formulario de creación y actualización de usuarios
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'bio', 'localidad', 'is_admin', 'is_moderator', 'is_representative', 'is_visitor')}
        ),
    )

    # Personalizar la búsqueda por los campos que se mostrarán en el panel
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    # Orden predeterminado de los usuarios en la lista
    ordering = ('username',)

# Registrar el modelo Usuario con la clase personalizada UsuarioAdmin
admin.site.register(Usuario, UsuarioAdmin)
