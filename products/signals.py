from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MovimentacaoEstoque

@receiver(post_save, sender=MovimentacaoEstoque)
def update_product_inventory(sender, instance, created, **kwargs):
    if created:
        produto = instance.produto
        if instance.tipo_movimento == 'entrada':
            produto.estoque_atual += instance.quantidade
        elif instance.tipo_movimento == 'saida':
            produto.estoque_atual -= instance.quantidade
        elif instance.tipo_movimento == 'ajuste':
            # caso o tipo de movimento seja ajuste, soma a quantidade informada ao estoque atual
            produto.estoque_atual += instance.quantidade
        
        produto.save()
