from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

def place_list(request):

    if request.method == 'POST':
        #create new place
        form = NewPlaceForm(request.POST)#creating a form from data request
        place = form.save() #creates model object from form
        if form.is_valid():#validate against DB constraints
            place.save()#saves place into DB
            return redirect('place_list')#redirects back to chosen page


    places = Place.objects.filter(visited = False).order_by('name')
    new_place_form = NewPlaceForm()
    #render = combining templates and data together
    return render(request, 'travel_wishlist/wishlist.html', {'places':places, 'new_place_form': new_place_form})

def places_visited(request):
    visited = Place.objects.filter(visited = True)
    return render(request,'travel_wishlist/visited.html', {'visited': visited})

def place_was_visited(request, place_id):
    if request.method == 'POST':
        #place = Place.objects.get(id=place_id)
        place = get_object_or_404(Place, id=place_id)
        place.visited = True
        place.save()

    return redirect('place_list')

def about(request):
    author = 'Stewart'
    about = 'This website is for listing desired travel destinations and being able to mark them as visited'
    return render(request, 'travel_wishlist/about.html', {'author':author, 'about': about})