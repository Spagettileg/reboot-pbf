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

""" Route to view a single rugby boot product on one page """
def single_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product_comment_form = ProductCommentForm(request.POST or None)
        if product_comment_form.is_valid():
            comment = request.POST.get('comment')
            product_comment = ProductComment.objects.create(product=product, creator=request.user, comment=comment)
            product_comment.save()
            messages.success(request, 'Thank you {} your comment has posted'.format(request.user), extra_tags="alert-success")
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        product_comment_form = ProductCommentForm()
        product.views += 1
        product.save()
    
    comments = ProductComment.objects.filter(product=product)
    
    product_comment_form = ProductCommentForm()
            
    context = {
        'product' : product,
        'product_comment_form': product_comment_form,
        'comments': comments,
    }
    
    return render(request, 'single_product.html', context)