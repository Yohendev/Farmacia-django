from django.db import models

class Medicamento(models.Model):
    CATEGORIAS_CHOICES = [
        ('analgesicos', 'Analgésicos'),
        ('antibioticos', 'Antibióticos'),
        ('uso-continuo', 'Uso Contínuo'),
        ('suplementos', 'Suplementos'),
    ]

    nome = models.CharField(
        max_length=150, 
        verbose_name="Nome do Produto"
    )
    apresentacao = models.CharField(
        max_length=200, 
        verbose_name="Apresentação / Descrição"
    )
    categoria = models.CharField(
        max_length=50, 
        choices=CATEGORIAS_CHOICES, 
        verbose_name="Categoria"
    )
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Preço de Venda"
    )
    quantidade = models.PositiveIntegerField(
        verbose_name="Quantidade em Estoque"
    )
    imagem = models.ImageField(
        upload_to='medicamentos/', 
        null=True, 
        blank=True, 
        verbose_name="Fotografia do Produto"
    )
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.apresentacao}"
    
    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        ordering = ['-criado_em']  