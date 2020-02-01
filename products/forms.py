from django import forms
from .models import Product
        
class ProductCreationForm(forms.ModelForm):
    """
    Form supports creation of a new rugby boot product. 
    """
    make = forms.CharField(max_length=254, required=True)
    """ No default product will be added into the database """
    category = forms.ChoiceField
    """ Category choices include view all, juniors and adults """
    customer = forms.ChoiceField
    """ Junior & Adult rugby players """
    size = forms.IntegerField()
    """ Size of the product """
    colour = forms.CharField(max_length=50, required=True)
    """ Product colour """
    studs = forms.CharField(max_length=50, required=True)
    """ Stud configuration of boot. Either moulded or screwin """
    quality = forms.CharField(max_length=50, required=True)
    """ Brand new, almost new and general wear """ 
    price = forms.DecimalField(max_digits=6, decimal_places=2, required=True)
    """ Pricing model will be less than £1m and decimal places = pence """
    image = forms.ImageField()
    """ Allow images to be uploaded for our products """
    
    class Meta:
        model = Product
        fields = ('make', 'category', 'customer', 'size', 'colour', 'studs', 'quality', 'price', 'image')