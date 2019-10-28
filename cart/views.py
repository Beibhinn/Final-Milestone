from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse


# Create your views here.
def view_cart(request):
    """A simple view that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a specified feature to the cart.
    No quantity needed as each feature the user wishes to support is separate"""
    donation_amount = int(request.POST.get('donation_amount'))
    print(donation_amount)
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + donation_amount
    else:
        cart[id] = cart.get(id, donation_amount)

    request.session['cart'] = cart
    print('added to cart')
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """
    Adjust the donation amount for the specified
    feature to a new amount
    """
    donation_amount = int(request.POST.get('donation_amount'))
    cart = request.session.get('cart', {})
    print('Got cart from session')

    if donation_amount > 0:
        cart[id] = donation_amount
        print('donation line')
    else:
        cart.pop(id)
        print('pop it')

    request.session['cart'] = cart
    print('session')
    return redirect(reverse('view_cart'))


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
