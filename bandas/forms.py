from django import forms
from .models import Banda, EstiloMusical, Integrante
from accounts.models import Usuario

#-------------------------------------------------------------------------------------------------------------

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nombre']  # Solo el nombre al principio

#-------------------------------------------------------------------------------------------------------------

class BiografiaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['biografia']  # Solo el campo de biografía es necesario para esta edición
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Escribe la biografía de la banda aquí...'})
        }

#-------------------------------------------------------------------------------------------------------------

class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = ['rol', 'instrumentos_favoritos', 'fecha_ingreso', 'genero_preferido', 'descripcion_personal', 'redes_sociales', 'imagen']
    
    banda = forms.ModelChoiceField(queryset=Banda.objects.all(), widget=forms.HiddenInput())