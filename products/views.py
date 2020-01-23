from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductComment
from django.utils import timezone
from django.contrib import messages
from .forms import ProductCommentForm, ProductCreationForm
from django.contrib.auth.decorators import login_required

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
def product_detail(request, pk):
    products = get_object_or_404(Product, pk=pk)
    context = {
        'product': products
    }
    return render(request, "productdetail.html", context)

""" Route allows the user to create (donate) a product """    
@login_required
def create_a_product(request):
    form = ProductCreationForm(request.POST)
    if request.method == "POST":
        
        if form.is_valid():
            product = form.save(commit=False)
            product.creator = request.user
            product.save()
            
            cart = request.session.get('cart', {})
            id = product.id
            cart[id] = cart.get(id, 1)
            request.session['cart'] = cart
            return redirect('checkout')
    else:
        form = ProductCreationForm()
    
    context = {
        'form' : form
    }
    
    return render(request, 'create_product.html', context)

""" Route permits user to delete their product(s) """     
@login_required
def delete_a_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        product.delete()
        messages.success(request, '{} your product has been deleted!'.format(request.user), extra_tags="alert-success")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, '{} sorry, your product cannot be deleted.'.format(request.user), extra_tags="alert-primary")
        return redirect(request.META.get('HTTP_REFERER'))