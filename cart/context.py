
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from tours.models import Tour


def cart_contents(request):

    cart_items = []
    total = 0
    tour_count = 0
    cart = request.session.get('cart', {})

    for item_id, participants in cart.items():
        tour = get_object_or_404(Tour, pk=item_id)
        total += participants * tour.cost
        cart_items.append({
            'item_id': item_id,
            'participants': participants,
            'tour': tour,
        })


    context = {
        'cart_items': cart_items,
        'total': total,
        'tour_count': tour_count,

    }

    return context