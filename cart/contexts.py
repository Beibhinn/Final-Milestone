from django.shortcuts import get_object_or_404
from features.models import Feature


def cart_contents(request):
    """
    Makes the cart contents available when rendering
    any page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    feature_count = 0

    for id, donation_amount in cart.items():
        feature = get_object_or_404(Feature, pk=id)
        total += donation_amount
        feature_count += 1
        cart_items.append({'id': id, 'donation_amount': donation_amount, 'feature': feature})

    return {'cart_items': cart_items, 'total': total, 'feature_count': feature_count}
