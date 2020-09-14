from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """ A view that renders the bag contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add Participants of the specified Tour to the cart"""

    participants = int(request.POST.get('participants'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    # Todo include here the code to manage the time of the booking, as size in example
    # you will need complete logic to manage day of the booking, because on cart same item must be displayed separately.

    if item_id in list(cart.keys()):
        cart[item_id] += participants
    else:
        cart[item_id] = participants

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
