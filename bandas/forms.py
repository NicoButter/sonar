from django import forms
from .models import Banda

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nombre', 'representante', 'estilos_musicales', 'biografia', 'demos', 'imagen', 'lugar_ensayo']
