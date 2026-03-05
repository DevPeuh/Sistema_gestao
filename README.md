# Sistema de Gestão Comercial - Loja de Materiais de Construção

Este é um sistema completo para gestão de estoque, compras, vendas e dashboard administrativo, desenvolvido com Django e Django REST Framework.

## Funcionalidades
- **Autenticação JWT**: Login seguro com tokens.
- **Gestão de Produtos**: Cadastro completo com SKU e imagens.
- **Controle de Estoque**: Atualização automática via signals.
- **Gestão de Compras**: Registro de NFs e contas a pagar.
- **Gestão de Vendas**: Registro de saídas e contas a receber.
- **Dashboard**: KPIs em tempo real.
- **Relatórios**: Exportação para PDF e Excel.

## Instalação

1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv .venv`
3. Ative o ambiente virtual.
4. Instale as dependências: `pip install -r requirements.txt`
5. Configure as variáveis de ambiente (`DATABASE_URL`, `SECRET_KEY`, etc.).
6. Execute as migrações: `python manage.py migrate`
7. Crie um superusuário: `python manage.py createsuperuser`
8. Inicie o servidor: `python manage.py runserver`

## API Endpoints
- `/api/token/`: Obter token JWT.
- `/api/categorias/`: CRUD de categorias.
- `/api/produtos/`: CRUD de produtos.
- `/api/compras/compras/`: CRUD de compras.
- `/api/vendas/vendas/`: CRUD de vendas.
- `/api/dashboard/stats/`: KPIs do sistema.
- `/api/reports/inventory/excel/`: Exportar estoque para Excel.
- `/api/reports/sales/pdf/`: Exportar vendas para PDF.

## Deploy
Configurado para deploy no Railway com PostgreSQL.

## Backup
Script `backup_db.py` configurado para ser executado via GitHub Actions.

## Testes
O sistema possui testes unitários e de integração integrados ao fluxo de desenvolvimento:
- **Testes Unitários**: Localizados em `products/tests.py`, validam modelos e labels.
- **Testes de Integração**: Arquivos `tests_integration.py` e `tests_unittest.py` fornecem cobertura para API e fluxos de negócio.
- **Verificação API**: `test_api.py` permite testes rápidos via `requests`.
- **Labels Amigáveis**: O Django Admin foi customizado para exibir labels intuitivos (ex: "Nome do Produto" em vez de "SKU").

Para executar os testes nativos:
```bash
python manage.py test
```
