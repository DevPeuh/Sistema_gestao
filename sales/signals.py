from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Venda, ItemVenda, ContaReceber
from products.models import MovimentacaoEstoque
from django.utils import timezone
from datetime import timedelta

@receiver(post_save, sender=Venda)
def create_conta_receber(sender, instance, created, **kwargs):
    if created:
        # Define um vencimento padrão de 30 dias se não houver lógica complexa
        ContaReceber.objects.create(
            venda=instance,
            cliente=instance.cliente,
            valor=instance.valor_total,
            data_vencimento=timezone.now().date() + timedelta(days=30),
            status='pendente'
        )

@receiver(post_save, sender=ItemVenda)
def create_inventory_movement_sale(sender, instance, created, **kwargs):
    if created:
        MovimentacaoEstoque.objects.create(
            produto=instance.produto,
            tipo_movimento='saida',
            quantidade=instance.quantidade,
            descricao=f"Venda ID {instance.venda.id}"
        )
