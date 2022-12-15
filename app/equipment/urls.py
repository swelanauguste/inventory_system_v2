from django.urls import path

from .views import (
    ComputerCreateView,
    ComputerListView,
    PrinterCreateView,
    PrinterListView,
)

app_name = "equip"

urlpatterns = [
    path("printers/", PrinterListView.as_view(), name="printer-list"),
    path("printer-create/", PrinterCreateView.as_view(), name="printer-create"),
    path("computers/", ComputerListView.as_view(), name="computer-list"),
    path("computer-create/", ComputerCreateView.as_view(), name="computer-create"),
]
