
from django.shortcuts import render
from .models import Tour

# Create your views here.


def all_tours(request):
    """ A view to show all tours available, including sorting and search queries """

    tours = Tour.objects.all()

    context = {
        'tours': tours,
    }

    return render(request, 'tours/tours.html', context)