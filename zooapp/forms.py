from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'especime', 'data_coleta']  # Incluindo os novos campos
