from rest_framework import serializers
from .models import Fornecedor, Compra, ItemCompra, ContaPagar

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class ItemCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCompra
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    itens = ItemCompraSerializer(many=True, read_only=True)
    
    class Meta:
        model = Compra
        fields = '__all__'

class ContaPagarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaPagar
        fields = '__all__'
