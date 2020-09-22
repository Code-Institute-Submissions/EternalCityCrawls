from django.shortcuts import render


def home(request):
    return render(
        request,
        'home/home.html'
    )

def error_404_view(request,exception):
    return render(request,'home/404.html')


def error_500_view(request):
    return render(request,'home/500.html')


