from django.contrib import admin
from .models import Medicamento

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apresentacao', 'categoria', 'tarja', 'preco', 'quantidade', 'em_estoque')
    
    search_fields = ('nome', 'apresentacao')
    
    list_filter = ('categoria', 'tarja', 'em_estoque')
    
    list_editable = ('preco', 'quantidade', 'em_estoque')
    
    readonly_fields = ('criado_em', 'atualizado_em')
    
    fieldsets = (
        ('Informações Principais', {
            'fields': ('nome', 'apresentacao', 'categoria', 'tarja')
        }),
        ('Estoque e Precificação', {
            'fields': ('preco', 'quantidade', 'em_estoque')
        }),
        ('Mídia', {
            'fields': ('imagem',)
        }),
        ('Auditoria', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )