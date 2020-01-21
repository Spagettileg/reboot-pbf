from django import forms
from .models import ProductComment, Product

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('comment',)
        
class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description')