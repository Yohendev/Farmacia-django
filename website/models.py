from django.db import models

class Medicamento(models.Model):
    CATEGORIAS_CHOICES = [
        ('analgesicos', 'Analgésicos'),
        ('antibioticos', 'Antibióticos'),
        ('uso-continuo', 'Uso Contínuo'),
        ('suplementos', 'Suplementos'),
        ('antidepressivo', 'Antidepressivo'),
        ('benzodiazepinico', 'Benzodiazepínico'),
        ('ansiolitico', 'Ansiolítico'),
        ('psicoestimulante', 'Psicoestimulante'),
        ('anticonvulsivante', 'Anticonvulsivante'),
        ('antipsicotico', 'Antipsicótico'),
    ]

    TARJA_CHOICES = [
        ('livre', 'Sem Tarja (Livre de Prescrição)'),
        ('amarela', 'Tarja Amarela (Genérico)'),
        ('vermelha_sem_retencao', 'Tarja Vermelha (Sem Retenção da Receita)'),
        ('vermelha_com_retencao', 'Tarja Vermelha (Com Retenção da Receita)'),
        ('preta', 'Tarja Preta'),
    ]

    nome = models.CharField(max_length=150)
    apresentacao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_CHOICES)
    tarja = models.CharField(max_length=50, choices=TARJA_CHOICES, default='livre')
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    em_estoque = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='medicamentos/', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.apresentacao}"
    
    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        ordering = ['-criado_em']