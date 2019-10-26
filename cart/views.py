from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse


# Create your views here.
def view_cart(request):
    """A simple view that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a specified feature to the cart.
    No quantity needed as each feature the user wishes to support is separate"""

    cart = request.session.get('cart', {})
    print('Got cart from session')
    cart[id] = cart.get(id)
    print('Got cart id')

    request.session['cart'] = cart
    print('added to cart')
    return redirect(reverse('index'))


def remove_from_cart(request, id):
    """
    Delete any specified feature from the cart
    """
    cart = request.session.get('cart', {})

    try:
        cart.pop(id)
    except e:
        return HttpResponse(status=500)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
