from rest_framework import serializers
from .models import Cliente, Venda, ItemVenda, ContaReceber

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    itens = ItemVendaSerializer(many=True, read_only=True)

    class Meta:
        model = Venda
        fields = '__all__'

class ContaReceberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaReceber
        fields = '__all__'
