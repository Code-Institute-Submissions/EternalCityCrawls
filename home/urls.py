from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name="home"),
    path('send/', views.contact_us, name="send_message")

]