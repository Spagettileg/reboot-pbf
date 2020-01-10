from django.shortcuts import render
from products.models import Product

# Product category views created here.
# View will consist of view all, junior and adult rugby boot products.

def product_filter(request, category):
    products = Product.objects.filter(category=category)
    return render(request, "products.html", {"products": products})