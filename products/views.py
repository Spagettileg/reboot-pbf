from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from django.utils import timezone
from django.contrib import messages
from .forms import ProductCreationForm
from django.contrib.auth.decorators import login_required
import sweetify


"""
Create product views
"""

""" View to show all products on a single page """


def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "products.html", context)


""" View to show Junior & Adult category for rugby boot shopping """


def categories(request):
    categories = Product.objects.all()
    context = {
        'categories': categories
    }
    return render(request, "products.html", context)


""" View to show rugby boot product detail, per product """


def product_detail(request, id):
    products = get_object_or_404(Product, id=id)
    context = {
        'product': products
    }
    return render(request, "productdetail.html", context)


""" Route allows the user to create (donate) a product """


@login_required
def create_a_product(request):

    if request.method == "POST":
        form = ProductCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            sweetify.success(request,
                             "Thank you {}, BootShop has been updated."
                             .format(request.user))

            return redirect('profile')
        else:
            form = ProductCreationForm()
            sweetify.error(request,
                           '{} sorry, your product cannot be added.'
                           .format(request.user))

    else:
        form = ProductCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'create_product.html', context)
