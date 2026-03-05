from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Compra, ItemCompra, ContaPagar
from products.models import MovimentacaoEstoque

@receiver(post_save, sender=Compra)
def create_conta_pagar(sender, instance, created, **kwargs):
    if created:
        ContaPagar.objects.create(
            compra=instance,
            fornecedor=instance.fornecedor,
            valor=instance.valor_total,
            data_vencimento=instance.data_vencimento,
            status='pendente'
        )

@receiver(post_save, sender=ItemCompra)
def create_inventory_movement(sender, instance, created, **kwargs):
    if created:
        MovimentacaoEstoque.objects.create(
            produto=instance.produto,
            tipo_movimento='entrada',
            quantidade=instance.quantidade,
            descricao=f"Compra NF {instance.compra.numero_nota_fiscal}"
        )
