from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.utils import timezone
from sales.models import Venda, ItemVenda
from purchases.models import Compra, ContaPagar
from sales.models import ContaReceber
from products.models import Produto
from datetime import timedelta

class DashboardStatsView(APIView):
    def get(self, request):
        today = timezone.now().date()
        month_start = today.replace(day=1)
        
        # Vendas do dia e mês
        vendas_dia = Venda.objects.filter(data_venda__date=today).aggregate(Sum('valor_total'))['valor_total__sum'] or 0
        vendas_mes = Venda.objects.filter(data_venda__date__gte=month_start).aggregate(Sum('valor_total'))['valor_total__sum'] or 0
        
        # Produtos mais vendidos (top 5)
        top_produtos = ItemVenda.objects.values('produto__descricao').annotate(total_vendido=Sum('quantidade')).order_by('-total_vendido')[:5]
        
        # Alertas de estoque baixo
        # Filtrar produtos onde estoque_atual <= estoque_minimo
        from django.db.models import F
        estoque_baixo = Produto.objects.filter(estoque_atual__lte=F('estoque_minimo')).count()
        
        # Contas a pagar/receber pendentes
        contas_pagar_pendentes = ContaPagar.objects.filter(status='pendente').aggregate(Sum('valor'))['valor__sum'] or 0
        contas_receber_pendentes = ContaReceber.objects.filter(status='pendente').aggregate(Sum('valor'))['valor__sum'] or 0
        
        return Response({
            'vendas_dia': vendas_dia,
            'vendas_mes': vendas_mes,
            'top_produtos': top_produtos,
            'estoque_baixo_count': estoque_baixo,
            'contas_pagar_pendentes': contas_pagar_pendentes,
            'contas_receber_pendentes': contas_receber_pendentes,
        })
