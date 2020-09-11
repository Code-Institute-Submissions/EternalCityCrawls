from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tours, name='tours'),
    path('<tour_id>', views.tour_detail, name='tour_details')
]