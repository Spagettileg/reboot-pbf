from django.shortcuts import render, redirect, reverse
from products.models import Product
from django.contrib import auth, messages
from django.db.models import Q

# Create your views here.

def search(request):
    """
    Search based on text input - returns products as a list 
    """
    products = None
    query = None
    product_count = 0
    
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.warning(request, 'Please enter a search criteria')
            return redirect(reverse('products'))
        products = Product.objects.all().filter(
            Q(make__icontains=query)
            | Q(category__icontains=query)
            | Q(customer__icontains=query)
            | Q(size__icontains=query)
            | Q(colour__icontains=query)
            | Q(studs__icontains=query)
            | Q(quality__icontains=query)
            | Q(price__icontains=query)
            )
        product_count = Product.objects.all().filter(
            Q(make__icontains=query)
            | Q(category__icontains=query)
            | Q(customer__icontains=query)
            | Q(size__icontains=query)
            | Q(colour__icontains=query)
            | Q(studs__icontains=query)
            | Q(quality__icontains=query)
            | Q(price__icontains=query)
            ).count()

        if product_count == 0:
            messages.warning(request, ('No results found'
                                       + f' for the search: {query}.'))
            return redirect(reverse('products'))

        context = {
            'query': query,
            'products': products,
            'count': product_count,
        }

        return render(request, 'search/search.html', context)

    return redirect(reverse('products'))