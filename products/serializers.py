from rest_framework import serializers
from .models import Produto, Categoria, UnidadeDeMedida, MovimentacaoEstoque

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class UnidadeDeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeDeMedida
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.ReadOnlyField(source='categoria.nome')
    unidade_sigla = serializers.ReadOnlyField(source='unidade_medida.sigla')

    class Meta:
        model = Produto
        fields = [
            'id', 'sku', 'descricao', 'categoria', 'categoria_nome', 
            'unidade_medida', 'unidade_sigla', 'preco_custo', 'preco_venda', 
            'estoque_atual', 'estoque_minimo', 'estoque_maximo', 
            'codigo_barras', 'imagem', 'criado_em', 'atualizado_em'
        ]
        extra_kwargs = {
            'sku': {'label': 'Nome do Produto'},
        }

class MovimentacaoEstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimentacaoEstoque
        fields = '__all__'
