from django.http import HttpResponse
from rest_framework.views import APIView
from products.models import Produto
from sales.models import Venda
import openpyxl
from reportlab.pdfgen import canvas
from io import BytesIO

class ExportInventoryExcelView(APIView):
    def get(self, request):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Estoque Atual"
        
        headers = ['SKU', 'Descrição', 'Estoque Atual', 'Estoque Mínimo', 'Preço de Venda']
        ws.append(headers)
        
        for produto in Produto.objects.all():
            ws.append([produto.sku, produto.descricao, produto.estoque_atual, produto.estoque_minimo, produto.preco_venda])
        
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=estoque.xlsx'
        wb.save(response)
        return response

class ExportSalesReportPDFView(APIView):
    def get(self, request):
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 800, "Relatório de Vendas")
        
        y = 780
        for venda in Venda.objects.all():
            p.drawString(100, y, f"Venda ID: {venda.id} - Cliente: {venda.cliente.nome} - Total: R$ {venda.valor_total}")
            y -= 20
            if y < 50:
                p.showPage()
                y = 800
        
        p.showPage()
        p.save()
        
        buffer.seek(0)
        return HttpResponse(buffer, content_type='application/pdf')
