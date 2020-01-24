from django import forms
from .models import Product
        
class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('make', 'category', 'customer', 'size', 'colour', 'studs', 'quality', 'price', 'image')