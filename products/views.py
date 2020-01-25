from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from django.utils import timezone
from django.contrib import messages
from .forms import ProductCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

def show_all_purchases(request):
    
    """
    Route to show all user purchases on one page
    """
    product_list = Product.objects.filter(created_date__lte=timezone.now(), paid=True).order_by('created_date')
    page = request.GET.get('page', 1)
    
    paginator = Paginator(product_list, 5)
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    context = {
        'products': products
    }
    return render(request, 'products.html', context)

""" Route allows the user to create (donate) a product """    
@login_required
def create_a_product(request):
    form = ProductCreationForm(request.POST)
    if request.method == "POST":
        
        if form.is_valid():
            product = form.save(commit=False)
            product.creator = request.user
            product.save()
            messages.success(request, "Thank you {0}, {1} has been added."
                             .format(request.user, product.make),
                             extra_tags="alert-primary")
            return redirect('profile')
    else:
        form = ProductCreationForm()
        messages.error(request, '{} sorry, your product cannot be added.'.format(request.user), extra_tags="alert-primary")
    
    context = {
        'form' : form
    }
    
    return render(request, 'create_product.html', context)
    
@login_required
def edit_a_product(request, pk):
    """
    Route to permit Re-Boot members to edit their rugby boot product
    """
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        form = ProductCreationForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.creator = request.user
            product.save()
            messages.success(request, "Thank you {0}, {1} has been updated."
                             .format(request.user, product.make),
                             extra_tags="alert-primary")
            return redirect(reverse('profile'))
    
    else:
        form = ProductCreationForm(instance=product)
        messages.error(request, '{} sorry, your product cannot be updated.'.format(request.user), extra_tags="alert-primary")
        
    context = {
        'form': form,
    }
    return render(request, 'edit_product.html', context)

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