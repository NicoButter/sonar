"""Formularios de la aplicación bandas.

Define los formularios ModelForm para la creación y edición de bandas,
biografías, integrantes e imágenes representativas.
"""

from django import forms

from accounts.models import Usuario  # noqa: F401
from .models import Banda, EstiloMusical, Integrante  # noqa: F401


class ImagenRepresentativaForm(forms.ModelForm):
    """Formulario para actualizar la imagen representativa de una banda.

    Permite subir o cambiar únicamente el campo ``imagen_principal``.
    """

    class Meta:
        model = Banda
        fields = ['imagen_principal']


class BandaForm(forms.ModelForm):
    """Formulario básico para crear o editar una banda.

    En su configuración inicial solo expone el campo ``nombre``.
    """

    class Meta:
        model = Banda
        fields = ['nombre']


class BiografiaForm(forms.ModelForm):
    """Formulario para editar la biografía de una banda.

    Incluye un widget Textarea personalizado con placeholder.
    """

    class Meta:
        model = Banda
        fields = ['biografia']
        widgets = {
            'biografia': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Escribe la biografía de la banda aquí...',
            }),
        }


class IntegranteForm(forms.ModelForm):
    """Formulario para crear o editar un integrante de banda.

    Incluye todos los campos del integrante excepto la banda,
    que se pasa como campo oculto.

    Attributes:
        banda: Campo oculto con la banda asociada.
    """

    banda = forms.ModelChoiceField(
        queryset=Banda.objects.all(), widget=forms.HiddenInput(),
    )

    class Meta:
        model = Integrante
        fields = [
            'rol', 'instrumentos_favoritos', 'fecha_ingreso',
            'genero_preferido', 'descripcion_personal',
            'redes_sociales', 'imagen',
        ]