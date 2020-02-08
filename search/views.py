from django.shortcuts import render
from products.models import Product
from django.contrib import auth, messages

# Create your views here.

def search(request):
    """
    Search based on text input - returns products as a list 
    """
    products = Product.objects.filter(
        make__icontains=request.GET['search'])
    return render(request, "products.html", {"products": products})
