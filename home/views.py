from django.shortcuts import render
from tours.models import Tour



def home(request):
    tours = Tour.objects.all()

    context = {
        'tours': tours,
    }

    return render(
        request,
        'home/home.html',
        context,
    )

def error_404_view(request,exception):
    return render(request,'home/404.html')


def error_500_view(request):
    return render(request,'home/500.html')


