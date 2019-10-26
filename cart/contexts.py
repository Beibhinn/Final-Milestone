from django.shortcuts import get_object_or_404
from features.models import Feature


def cart_contents(request):
    """
    Makes the cart contents available when rendering
    any page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    feature_count = 0

    for key, value in cart.items():
        feature = get_object_or_404(Feature, pk=key)
        feature_count += 1
        cart_items.append({'id': key, 'feature': feature})

    return {'cart_items': cart_items, 'feature_count': feature_count}
