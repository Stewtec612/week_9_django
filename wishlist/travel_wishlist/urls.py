from django.urls import path
from . import views

#urls the app will recognize
urlpatterns = [
    path('', views.place_list, name = 'place_list'),#creates place_list url
    path('visited', views.places_visited, name='places_visited'),#creates /places_visited url
    path('about', views.about, name='about'),#creates /about url
    path('place/<int:place_id>/was_visited', views.place_was_visited, name='place_was_visited'),#Using id because it is represented by id in db
    path('place/<int:place_id>', views.place_details, name='place_details'),# creates url for each individual place in the users list
    path('place/<int:place_id>/delete', views.delete_place, name='delete_place')
    ]