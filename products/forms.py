from django import forms
from .models import Product


class ProductCreationForm(forms.ModelForm):
    """
    Placeholder messages guides the user in donating a new rugby boot product.
    """

    make = forms.CharField(widget=forms.TextInput
                           ({'placeholder': 'Nike'}),
                           required=True)
    """ User required to add a rugby boot brand name """
    category = forms.CharField(widget=forms.TextInput
                              ({'placeholder': 'Juniors'}),
                              required=True)
    """ Category choices include juniors and adults only  """
    customer = forms.CharField(widget=forms.TextInput
                              ({'placeholder': 'Juniors'}),
                              required=True)
    """ Junior or adult rugby players. Customer choice must match category """
    size = forms.IntegerField(widget=forms.NumberInput
                             ({'placeholder': '11'}),
                             required=True)
    """ 
    Size of the product. Guidelines created for user to determine sizes
    for both juniors and adults
    """
    colour = forms.CharField(widget=forms.TextInput
                            ({'placeholder': 'Blue'}),
                            required=True)
    """
    Product colour will help the Re-Boot community in the absence of
    an uploaded product image
    """
    studs = forms.CharField(widget=forms.TextInput
                           ({'placeholder': 'Screw in'}),
                           required=True)
    """ Stud configuration of boot. Either moulded or screwin """
    quality = forms.CharField(widget=forms.TextInput
                             ({'placeholder': 'Used Boots'}),
                             required=True)
    """
    Brand new, almost new and used boots. There is further help for
    the user when accessing 'about' > 'bootquality' from the navbar
    """
    price = forms.DecimalField(widget=forms.NumberInput
                              ({'placeholder': '5'}),
                              required=True)
    """ Pricing model £5 for all junior boots and £10 for all adult boots """

    class Meta:
        model = Product
        fields = ('make', 'category', 'customer', 'size', 'colour', 'studs',
                  'quality', 'price', 'image')
