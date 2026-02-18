"""Modelos de la aplicación bandas.

Define los modelos principales del dominio musical: bandas, integrantes,
estilos musicales, imágenes y flyers. También incluye las funciones
auxiliares para generar las rutas de almacenamiento de archivos.
"""

import os

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

from accounts.models import Usuario


# ---------------------------------------------------------------------------
# Funciones de ruta de almacenamiento
# ---------------------------------------------------------------------------

def banda_directory_path(instance, filename):
    """Genera la ruta de almacenamiento para demos de una banda.

    Args:
        instance: Instancia del modelo Banda.
        filename: Nombre original del archivo subido.

    Returns:
        Ruta relativa con formato ``bandas/<slug>/demos/<filename>``.
    """
    return os.path.join('bandas', slugify(instance.nombre), 'demos', filename)


def banda_imagen_representativa_path(instance, filename):
    """Genera la ruta de almacenamiento para la imagen representativa.

    Args:
        instance: Instancia del modelo Banda.
        filename: Nombre original del archivo subido.

    Returns:
        Ruta relativa con formato ``<slug>/imagenes/representativa/<filename>``.
    """
    return os.path.join(
        slugify(instance.nombre), 'imagenes', 'representativa', filename,
    )


def banda_imagen_directory_path(instance, filename):
    """Genera la ruta de almacenamiento para imágenes de la banda.

    Args:
        instance: Instancia de un modelo con FK a Banda.
        filename: Nombre original del archivo subido.

    Returns:
        Ruta relativa con formato ``<slug>/imagenes_de_la_banda/<filename>``.
    """
    return os.path.join(
        slugify(instance.banda.nombre), 'imagenes_de_la_banda', filename,
    )


def integrante_imagen_directory_path(instance, filename):
    """Genera la ruta de almacenamiento para imágenes de integrantes.

    Args:
        instance: Instancia del modelo Integrante.
        filename: Nombre original del archivo subido.

    Returns:
        Ruta relativa con formato ``<slug>/imagenes_de_integrantes/<filename>``.
    """
    return os.path.join(
        slugify(instance.banda.nombre), 'imagenes_de_integrantes', filename,
    )


def flyer_imagen_directory_path(instance, filename):
    """Genera la ruta de almacenamiento para flyers de la banda.

    Args:
        instance: Instancia del modelo Flyer.
        filename: Nombre original del archivo subido.

    Returns:
        Ruta relativa con formato ``<slug>/flyers/<filename>``.
    """
    return os.path.join(
        slugify(instance.banda.nombre), 'flyers', filename,
    )


# ---------------------------------------------------------------------------
# Modelos
# ---------------------------------------------------------------------------

class EstiloMusical(models.Model):
    """Modelo que representa un estilo o género musical.

    Attributes:
        nombre: Nombre único del estilo musical.
    """

    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """Retorna el nombre del estilo musical."""
        return self.nombre


class Banda(models.Model):
    """Modelo principal que representa una banda musical.

    Almacena la información general de la banda, incluyendo su nombre,
    representante, estilos musicales, biografía, archivos multimedia
    y estado de moderación.

    Attributes:
        nombre: Nombre único de la banda.
        representante: Usuario con rol de representante asociado a la banda.
        estilos_musicales: Relación muchos-a-muchos con EstiloMusical.
        biografia: Texto descriptivo sobre la historia de la banda.
        demos: Archivo de audio/demo de la banda.
        imagen_principal: Imagen representativa de la banda.
        imagen: Imagen adicional de la banda.
        lugar_ensayo: Dirección o nombre del lugar de ensayo.
        fecha_creacion: Fecha de registro de la banda (auto-generada).
        estado: Estado de moderación ('pendiente', 'aprobado', 'rechazado').
    """

    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    representante = models.OneToOneField(
        Usuario, on_delete=models.CASCADE,
        related_name='banda', null=True, blank=True,
    )
    estilos_musicales = models.ManyToManyField(EstiloMusical)
    biografia = models.TextField()
    demos = models.FileField(
        upload_to=banda_directory_path, blank=True, null=True,
    )
    imagen_principal = models.ImageField(
        upload_to=banda_imagen_representativa_path, blank=True, null=True,
    )
    imagen = models.ImageField(
        upload_to=banda_imagen_directory_path, blank=True, null=True,
    )
    lugar_ensayo = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20, choices=ESTADOS, default='pendiente',
    )

    def clean(self):
        """Valida que el representante tenga el rol correspondiente.

        Raises:
            ValidationError: Si el usuario asignado no tiene el rol
                de representante.
        """
        if not self.representante.is_representative:
            raise ValidationError(
                'El usuario asignado como representante debe tener '
                'el rol de representante.'
            )

    def __str__(self):
        """Retorna el nombre de la banda."""
        return self.nombre


class Integrante(models.Model):
    """Modelo que representa un integrante de una banda.

    Attributes:
        banda: Banda a la que pertenece el integrante.
        rol: Rol o puesto del integrante en la banda.
        instrumentos_favoritos: Instrumentos que toca o prefiere.
        fecha_ingreso: Fecha en que ingresó a la banda.
        genero_preferido: Género musical preferido del integrante.
        descripcion_personal: Texto libre sobre el integrante.
        redes_sociales: Diccionario JSON con URLs de redes sociales.
        imagen: Foto del integrante.
    """

    banda = models.ForeignKey(
        Banda, on_delete=models.CASCADE, related_name='integrantes',
    )
    rol = models.CharField(max_length=100)
    instrumentos_favoritos = models.CharField(max_length=200)
    fecha_ingreso = models.DateField()
    genero_preferido = models.CharField(
        max_length=100, blank=True, null=True,
    )
    descripcion_personal = models.TextField(blank=True, null=True)
    redes_sociales = models.JSONField(default=dict, blank=True, null=True)
    imagen = models.ImageField(
        upload_to=integrante_imagen_directory_path, blank=True, null=True,
    )

    class Meta:
        """Meta opciones para Integrante."""

        unique_together = ('banda', 'rol')

    def __str__(self):
        """Retorna el nombre de la banda y el rol del integrante."""
        return f'{self.banda.nombre} - {self.rol}'


class ImagenBanda(models.Model):
    """Modelo para almacenar imágenes adicionales de una banda.

    Attributes:
        banda: Banda propietaria de la imagen.
        imagen: Archivo de imagen.
        fecha_subida: Fecha y hora de subida (auto-generada).
    """

    banda = models.ForeignKey(
        Banda, on_delete=models.CASCADE, related_name='imagenes',
    )
    imagen = models.ImageField(upload_to=banda_imagen_directory_path)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta opciones para ImagenBanda."""

        unique_together = ('banda', 'id')

    def __str__(self):
        """Retorna una descripción con el nombre de la banda y el ID."""
        return f"Imagen de {self.banda.nombre} - {self.id}"


class Flyer(models.Model):
    """Modelo para almacenar flyers promocionales de una banda.

    Attributes:
        banda: Banda propietaria del flyer.
        imagen: Archivo de imagen del flyer.
        descripcion: Descripción opcional del flyer.
    """

    banda = models.ForeignKey(
        Banda, on_delete=models.CASCADE, related_name='flyers',
    )
    imagen = models.ImageField(upload_to=flyer_imagen_directory_path)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        """Retorna una descripción con el nombre de la banda."""
        return f"Flyer de {self.banda.nombre}"
