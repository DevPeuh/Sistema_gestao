from rest_framework import viewsets
from .models import Cliente, Venda, ItemVenda, ContaReceber
from .serializers import ClienteSerializer, VendaSerializer, ItemVendaSerializer, ContaReceberSerializer

# aqui estão as viewsets para os modelos Cliente, Venda, ItemVenda e ContaReceber
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class ItemVendaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer

class ContaReceberViewSet(viewsets.ModelViewSet):
    queryset = ContaReceber.objects.all()
    serializer_class = ContaReceberSerializer
