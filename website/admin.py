from django.contrib import admin
from .models import Medicamento

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'quantidade', 'atualizado_em')
    list_filter = ('categoria',)
    search_fields = ('nome', 'apresentacao')
    readonly_fields = ('criado_em', 'atualizado_em')