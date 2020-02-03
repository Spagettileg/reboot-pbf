from django import forms
from .models import Product
        
class ProductCreationForm(forms.ModelForm):
    """
    Form supports creation of a new rugby boot product. 
    """
   
    class Meta:
        model = Product
        fields = ('make', 'category', 'customer', 'size', 'colour', 'studs', 'quality', 'price', 'image')