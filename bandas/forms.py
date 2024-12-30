from django import forms
from .models import Banda, EstiloMusical, Integrante
from accounts.models import Usuario

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nombre']  # Solo el nombre al principio


# class BandaForm(forms.ModelForm):
#     class Meta:
#         model = Banda
#         fields = ['nombre', 'representante', 'estilos_musicales', 'biografia', 'demos', 'imagen', 'lugar_ensayo', 'estado']
    
#     representante = forms.ModelChoiceField(queryset=Usuario.objects.filter(is_representative=True), label="Representante")
#     estilos_musicales = forms.ModelMultipleChoiceField(queryset=EstiloMusical.objects.all(), widget=forms.CheckboxSelectMultiple)

class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = ['rol', 'instrumentos_favoritos', 'fecha_ingreso', 'genero_preferido', 'descripcion_personal', 'redes_sociales', 'imagen']
    
    banda = forms.ModelChoiceField(queryset=Banda.objects.all(), widget=forms.HiddenInput())