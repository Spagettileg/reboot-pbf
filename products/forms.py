from django import forms
from .models import ProductComment, Product

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('comment',)
        
class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('make', 'category', 'customer', 'size', 'colour', 'studs', 'quality', 'price', 'image', 'creator')