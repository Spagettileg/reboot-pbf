from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def view_cart(request):
    """
    A view that renders the shopping cart showing all contents page
    """
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """
    Add a unique product to shopping cart within the session.
    Cart item are not stored in the database, but in the shopping cart.
    """
    quantity = int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    
    # If statement ensures a product price is not updated via User adding
    # a duplicate product.
    
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    print("quantity:")
    print(quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, id):
    """
    Remove a product from the cart.
    """
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect('view_cart')