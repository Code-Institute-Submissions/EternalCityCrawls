
from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    cart_items = []
    total = 0
    tour_count = 0

    context = {
        'bag_items': cart_items,
        'total': total,
        'tour_count': tour_count,

    }

    return context