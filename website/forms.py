from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nome', 'apresentacao', 'categoria', 'tarja', 'preco', 'quantidade', 'em_estoque', 'imagem']