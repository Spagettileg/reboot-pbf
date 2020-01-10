from django.shortcuts import render, get_object_or_404
from .models import Product

"""
Create product views
"""
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def product_detail(request, pk):
    products = get_object_or_404(Product, pk=pk)
    return render(request, "productdetail.html", {"product": products})
