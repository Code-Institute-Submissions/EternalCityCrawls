from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from tours.models import Tour

# Create your views here.

def view_cart(request):
    """Render Cart
    Args:
        request: http request
    Returns:
        render cart template
    """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """Add tour to the cart
    Args:
        request: http request
        item_id: Tour to add id
    Returns:
        redirect request
    """

    tour = get_object_or_404(Tour, pk=item_id)
    participants = int(request.POST.get('participants'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += participants
        messages.success(request, f"updated participants to {tour.name}")

    else:
        cart[item_id] = participants
        messages.success(request, f"{tour.name} added to the cart")


    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """update tour in the cart
    Args:
        request: http request
        item_id: id tour to update
    Returns:
        redirect request
    """

    tour = get_object_or_404(Tour, pk=item_id)
    participants = int(request.POST.get('participants'))

    cart = request.session.get('cart', {})


    if participants > 0:
        cart[item_id] = participants
        messages.success(request, f"updated participants to {tour.name}")


    else:
        cart.pop(item_id)
        messages.success(request, f"{tour.name} removed from the cart")

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):
    """remove tour from the cart
    Args:
        request: http request
        item_id: id tour to delete
    Returns:
        redirect request
    """

    tour = get_object_or_404(Tour, pk=item_id)
    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        messages.success(request, f"{tour.name} removed from the cart")
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"error removing {tour.name} from the cart")
        return HttpResponse(status=500)
