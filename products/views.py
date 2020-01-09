from django.shortcuts import render
from django.views.generic import CreateView
from .models import Product

def ProductCreateView(request, CreateView):
    model = Product
    products = ('make', 'size', 'colour', 'studs', 'price', 'image')
    return render(request, "products.html", {"products": products, "model": model})


