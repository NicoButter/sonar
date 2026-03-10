"""Configuración del panel de administración para la aplicación bandas."""

from django.contrib import admin

from .models import Banda, EstiloMusical, Flyer, ImagenBanda, Integrante, Evento


class IntegranteInline(admin.TabularInline):
    """Inline para gestionar integrantes desde la vista de Banda."""

    model = Integrante
    extra = 1


class ImagenBandaInline(admin.TabularInline):
    """Inline para gestionar imágenes desde la vista de Banda."""

    model = ImagenBanda
    extra = 1


class FlyerInline(admin.TabularInline):
    """Inline para gestionar flyers desde la vista de Banda."""

    model = Flyer
    extra = 1


@admin.register(Banda)
class BandaAdmin(admin.ModelAdmin):
    """Configuración del admin para el modelo Banda."""

    list_display = ('nombre', 'representante', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'estilos_musicales', 'fecha_creacion')
    search_fields = ('nombre', 'representante__username')
    inlines = [IntegranteInline, ImagenBandaInline, FlyerInline]


@admin.register(EstiloMusical)
class EstiloMusicalAdmin(admin.ModelAdmin):
    """Configuración del admin para el modelo EstiloMusical."""

    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    """Configuración del admin para el modelo Integrante."""

    list_display = ('banda', 'rol', 'fecha_ingreso')
    list_filter = ('banda',)
    search_fields = ('banda__nombre', 'rol')


@admin.register(ImagenBanda)
class ImagenBandaAdmin(admin.ModelAdmin):
    """Configuración del admin para el modelo ImagenBanda."""

    list_display = ('banda', 'fecha_subida')
    list_filter = ('banda',)


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    """Configuración del admin para el modelo Evento."""

    list_display = ('titulo', 'fecha', 'ubicacion', 'organizador', 'fecha_creacion')
    list_filter = ('fecha', 'ubicacion')
    search_fields = ('titulo', 'descripcion', 'ubicacion')
    date_hierarchy = 'fecha'
