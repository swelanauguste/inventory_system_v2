from django import forms

from .models import Equipment


class EquipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = "__all__"
