from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import EquipmentCreateForm
from .models import Equipment, Group


class PrinterCreateView(CreateView):
    model = Equipment
    form_class = EquipmentCreateForm
    success_url = reverse_lazy("equip:printer-list")


class PrinterListView(ListView):
    model = Equipment
    printer = Group.objects.get(name__icontains="printer")
    extra_context = {
        "printer_create_form": EquipmentCreateForm(initial={"group": printer})
    }
    template_name = 'equipment/printer_list.html'
    
    def get_queryset(self):
        queryset = Equipment.objects.filter(group__name__icontains='printer')
        return queryset

class ComputerCreateView(CreateView):
    model = Equipment
    form_class = EquipmentCreateForm
    success_url = reverse_lazy("equip:computer-list")


class ComputerListView(ListView):
    model = Equipment
    computer = Group.objects.get(name__icontains="computer")
    extra_context = {
        "computer_create_form": EquipmentCreateForm(initial={"group": computer})
    }
    template_name = 'equipment/computer_list.html'
    
    def get_queryset(self):
        queryset = Equipment.objects.filter(group__name__icontains='computer')
        return queryset
    
