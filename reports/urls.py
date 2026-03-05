from django.urls import path
from .views import ExportInventoryExcelView, ExportSalesReportPDFView

urlpatterns = [
    path('inventory/excel/', ExportInventoryExcelView.as_view(), name='export-inventory-excel'),
    path('sales/pdf/', ExportSalesReportPDFView.as_view(), name='export-sales-pdf'),
]
