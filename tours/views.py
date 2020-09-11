
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Tour

# Create your views here.


def all_tours(request):
    """ A view to show all tours available, including sorting and search queries """

    tours = Tour.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('tours'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            tours = tours.filter(queries)

    context = {
        'tours': tours,
        'search_term': query,

    }

    return render(request, 'tours/tours.html', context)