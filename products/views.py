from rest_framework import viewsets
from .models import Produto, Categoria, UnidadeDeMedida, MovimentacaoEstoque
from .serializers import ProdutoSerializer, CategoriaSerializer, UnidadeDeMedidaSerializer, MovimentacaoEstoqueSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class UnidadeDeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadeDeMedida.objects.all()
    serializer_class = UnidadeDeMedidaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class MovimentacaoEstoqueViewSet(viewsets.ModelViewSet):
    queryset = MovimentacaoEstoque.objects.all()
    serializer_class = MovimentacaoEstoqueSerializer
