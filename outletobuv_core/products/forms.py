from .models import Product
from django import forms


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'image']
