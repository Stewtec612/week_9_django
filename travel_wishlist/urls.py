from django.urls import path
from . import views

#urls the app will recognize
urlpatterns = [
    path('', views.place_list, name = 'place_list'),
    path('visited', views.places_visited, name='places_visited'),
    path('about', views.about, name='about'),
    path('place/<int:place_id>/was_visited', views.place_was_visited, name='place_was_visited')#Using id because it is represented by id

]