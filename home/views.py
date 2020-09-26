from django.shortcuts import render, redirect
from tours.models import Tour
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



def home(request):
    tours = Tour.objects.all().order_by('-rating')[:8]
    contact_form = ContactForm()

    context = {
        'tours': tours,
        'contact_form': contact_form
    }

    return render(
        request,
        'home/home.html',
        context,
    )

def contact_us(request):
    """
    Returns the contact_us.html page and allows user to post contact forms
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            message = contact_form.cleaned_data['message']
            from_email = contact_form.cleaned_data['email']
            send_mail(
            name,
            message,
            settings.DEFAULT_CONTACT_EMAIL, # here is from the user
            [settings.CONTACT_RECIPIENT]
        )  
            messages.success(
                request, "Your message has been sent, we will be in touch soon.")
            return redirect('send_message')
    else:
        contact_form = ContactForm()

    return render(request, 'home/home.html', { 'contact_form': contact_form})

def error_404_view(request,exception):
    return render(request,'home/404.html')


def error_500_view(request):
    return render(request,'home/500.html')


