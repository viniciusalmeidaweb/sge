from django import forms
from . import models

class BrandForm(forms.ModelForm):

    class Meta:
        model = models.Brand
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rrows': 3}),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }
