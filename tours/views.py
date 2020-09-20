
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Tour, Category
from .forms import TourForm

# Create your views here.


def all_tours(request):
    """ A view to show all tours available, including sorting and search queries """

    tours = Tour.objects.all()
    query = None
    sort = None
    direction = None
    categories = None


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == "name":
                sortkey = 'lower_name'
                tours = tours.annotate(lower_name=Lower("name"))
            if sortkey == 'category':
                sortkey = 'category__name'
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

@login_required
def add_tour(request):
    """ Add a Tour to the catalogue """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Tour Manager can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            tour = form.save()
            messages.success(request, 'Successfully added Tour!')
            return redirect(reverse('tour_detail', args=[tour.id]))
        else:
            messages.error(request, 'Failed to add tour. Please ensure the form is valid.')
    else:
        form = TourForm()
    template = 'tours/add_tour.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def update_tour(request, tour_id):
    """ Update a tour in the catalogue """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Tour Manager can do that.')
        return redirect(reverse('home'))

    tour = get_object_or_404(Tour, pk=tour_id)
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('tour_details', args=[tour.id]))
        else:
            messages.error(request, 'Failed to update tour. Please ensure the form is valid.')
    else:
        form = TourForm(instance=tour)
        messages.info(request, f'You are editing {tour.name}')

    template = 'tours/update_tour.html'
    context = {
        'form': form,
        'tour': tour,
    }
    return render(request, template, context)

@login_required
def delete_tour(request, tour_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Tour Manager can do that.')
        return redirect(reverse('home'))
    tour = get_object_or_404(Tour, pk=tour_id)
    tour.delete()
    messages.success(request, 'Tour deleted!')
    return redirect(reverse('tours'))