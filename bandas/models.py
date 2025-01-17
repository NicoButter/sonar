from django.db import models
from accounts.models import Usuario  # Relación con el modelo Usuario
import os
from django.utils.text import slugify
from django.core.exceptions import ValidationError


#-------------------------------------------------------------------------------------------------------------------

class EstiloMusical(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre

#-------------------------------------------------------------------------------------------------------------------

def banda_directory_path(instance, filename):
    return os.path.join('bandas', slugify(instance.nombre), 'demos', filename)

def banda_imagen_directory_path(instance, filename):
    return os.path.join('bandas', slugify(instance.banda.nombre), 'imagenes_de_la_banda', filename)

def integrante_imagen_directory_path(instance, filename):
    return os.path.join('bandas', slugify(instance.banda.nombre), 'imagenes_de_integrantes', filename)

def flyer_imagen_directory_path(instance, filename):
    return os.path.join('bandas', slugify(instance.banda.nombre), 'flyers', filename)

#-------------------------------------------------------------------------------------------------------------------

class Banda(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    representante = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='banda', null=True, blank=True)
    estilos_musicales = models.ManyToManyField(EstiloMusical)
    biografia = models.TextField()
    demos = models.FileField(upload_to=banda_directory_path, blank=True, null=True)
    imagen = models.ImageField(upload_to=banda_imagen_directory_path, blank=True, null=True)
    lugar_ensayo = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    # Estado para moderación
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]
    estado = models.CharField(
        max_length=20, choices=ESTADOS, default='pendiente'
    )

    def clean(self):
        # Validación para asegurar que el representante tiene el rol adecuado
        if not self.representante.is_representative:
            raise ValidationError('El usuario asignado como representante debe tener el rol de representante.')
    
    def __str__(self):
        return self.nombre

#-------------------------------------------------------------------------------------------------------------------

class Integrante(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='integrantes')
    rol = models.CharField(max_length=100)
    instrumentos_favoritos = models.CharField(max_length=200)
    fecha_ingreso = models.DateField()
    genero_preferido = models.CharField(max_length=100, blank=True, null=True)
    descripcion_personal = models.TextField(blank=True, null=True)
    redes_sociales = models.JSONField(default=dict, blank=True, null=True)  # Guarda URLs de redes sociales
    imagen = models.ImageField(upload_to=integrante_imagen_directory_path, blank=True, null=True)

    def __str__(self):
        return f'{self.banda.nombre} - {self.rol}'

    class Meta:
        unique_together = ('banda', 'rol')  # Asegura que cada banda no tenga más de un integrante con el mismo rol

#-------------------------------------------------------------------------------------------------------------------

class ImagenBanda(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to=banda_imagen_directory_path)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagen de {self.banda.nombre} - {self.id}"
    
    class Meta:
        # Limitar a un máximo de 5 imágenes por banda
        unique_together = ('banda', 'id')  # Esto no es necesario, pero te lo dejo como referencia

#-------------------------------------------------------------------------------------------------------------------

class Flyer(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='flyers')
    imagen = models.ImageField(upload_to=flyer_imagen_directory_path)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"Flyer de {self.banda.nombre}"
