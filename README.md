# Sistema de Gestão Comercial - Loja de Materiais de Construção

Sistema robusto e escalável desenvolvido para a digitalização completa de processos comerciais em lojas de materiais de construção. A solução substitui controles manuais por uma plataforma digital integrada, focada em integridade de dados e eficiência operacional.

## 🏛️ Arquitetura do Sistema

O projeto segue a arquitetura **Monolítica Modularizada** utilizando o framework Django, com uma camada de API robusta via **Django REST Framework (DRF)**.

### Camadas Principais:
- **Core (gestao_comercial)**: Configurações globais, segurança e roteamento principal.
- **Módulos de Negócio**: Divisão por aplicativos Django especializados, cada um com seus próprios modelos, serializers, views e lógica de sinais.
- **Data Layer**: PostgreSQL como banco de dados relacional, utilizando constraints de integridade e triggers para auditoria.
- **Middleware Layer**: Logs de acesso e segurança customizados.

## 🚀 Tecnologias Empregadas

- **Backend**: Python 3.13 / Django 6.0
- **API**: Django REST Framework (DRF) com autenticação JWT (SimpleJWT)
- **Banco de Dados**: PostgreSQL 14+
- **Segurança**: Proteção CSRF, XSS, Rate Limiting e Criptografia Bcrypt
- **Documentação Técnica**: Docstrings em conformidade com PEP 257
- **Geração de Documentos**: ReportLab (PDF) e OpenPyXL (Excel)

## 📂 Estrutura de Pastas e Módulos

```text
Sistema_Gestao/
├── dashboard/          # KPIs em tempo real e Logs de Acesso
├── products/           # Gestão de Produtos, Categorias e Controle de Estoque
├── purchases/          # Fornecedores, Notas Fiscais de Entrada e Contas a Pagar
├── sales/              # Clientes, Vendas (PDV) e Contas a Receber
├── reports/            # Motores de exportação (PDF/Excel)
├── gestao_comercial/   # Configurações do Projeto (Settings/URLs)
└── .github/            # Workflows de CI/CD e Backups Automáticos
```

## 🛠️ Principais Componentes e Funcionalidades

### 1. Módulo de Autenticação e Segurança
- Autenticação baseada em tokens JWT para comunicação stateless segura.
- Middleware de auditoria para registro de todos os acessos por IP, usuário e endpoint.

### 2. Gestão de Produtos e Inventário
- Cadastro técnico com SKU, descrição, unidade de medida e precificação dinâmica.
- **Controle Automático de Estoque**: Implementação via Signals que processa entradas e saídas em tempo real, mantendo o saldo atualizado.
- Alertas de estoque crítico baseados em níveis mínimos configuráveis.

### 3. Fluxo de Compras (Suprimentos)
- Gestão de fornecedores e registro de Notas Fiscais.
- Automação financeira: Geração imediata de títulos no Contas a Pagar após validação de entrada de mercadoria.

### 4. Fluxo de Vendas (Comercial)
- Gestão de carteira de clientes e registro de saídas.
- Integração financeira: Lançamento automático no Contas a Receber e atualização instantânea de inventário.

### 5. Inteligência de Negócio (Dashboard)
- Consolidação de KPIs: Vendas diárias/mensais, curva de produtos mais vendidos e visão geral de inadimplência.

### 6. Sistema de Relatórios
- Exportação de dados valorizados de estoque e histórico de vendas para conformidade contábil e administrativa.
