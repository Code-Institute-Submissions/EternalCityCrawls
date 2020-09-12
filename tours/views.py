
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Tour, Category

# Create your views here.


def all_tours(request):
    """ A view to show all tours available, including sorting and search queries """

    tours = Tour.objects.all()
    query = None
    sort = None
    categories = None


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == "name":
                sortkey = 'lower_name'
                tours = tours.annotate(lower_name=Lower("name"))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'

            tours = tours.order_by(sortkey)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            tours = tours.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('tours'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            tours = tours.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'tours': tours,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'tours/tours.html', context)


def tour_detail(request, tour_id):
    """ A view to show the details of a specific tour """

    tour = get_object_or_404(Tour,pk=tour_id)


    context = {
        'tour': tour,

    }

    return render(request, 'tours/tour_details.html', context)