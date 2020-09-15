from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from tours.models import Tour

# Create your views here.

def view_cart(request):
    """ A view that renders the bag contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add Participants of the specified Tour to the cart"""

    tour = Tour.objects.get(pk=item_id)
    participants = int(request.POST.get('participants'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    # Todo include here the code to manage the time of the booking, as size in example
    # you will need complete logic to manage day of the booking, because on cart same item must be displayed separately.

    if item_id in list(cart.keys()):
        cart[item_id] += participants
    else:
        cart[item_id] = participants
        messages.success(request, f"{tour.name} added to the cart")


    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """update participants in cart"""

    participants = int(request.POST.get('participants'))

    cart = request.session.get('cart', {})


    if participants > 0:
        cart[item_id] = participants
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):
    """Remove the item from the cart"""

    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
