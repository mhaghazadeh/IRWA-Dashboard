
from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        exclude = ['created_by', 'created_at']
        widgets = {
            'date_received': forms.DateInput(attrs={'type': 'date'}),
            'radionuclides': forms.CheckboxSelectMultiple()
        }