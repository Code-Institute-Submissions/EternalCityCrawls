from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tours, name='tours'),
    path('<int:tour_id>', views.tour_detail, name='tour_details'),
    path('add/', views.add_tour, name='add_tour'),
    path('update/<int:tour_id>/', views.update_tour, name='update_tour'),
    path('delete/<int:tour_id>/', views.delete_tour, name='delete_tour'),

]