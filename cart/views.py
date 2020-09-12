from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ A view that renders the bag contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add Participants of the specified Tour to the cart"""

    participants = int(request.POST.get('participants'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += participants
    else:
        cart[item_id] = participants

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
