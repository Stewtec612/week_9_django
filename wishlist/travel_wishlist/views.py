
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import TripReviewForm

@login_required #one user name required
def place_list(request): 
    '''
    Incharge of creating and controlling the place list on wishlist homepage
        -it can add user entered names of places and save them to a list
    '''

    if request.method == 'POST':
        #create new place
        form = NewPlaceForm(request.POST)#creating a form from data request
        place = form.save(commit=False) #creates model object from form
        place.user = request.user
        
        if form.is_valid():#validate against DB constraints
            place.save()#saves place into DB
            return redirect('place_list')#redirects back to chosen page


    
    places = Place.objects.filter(user=request.user, visited = False).order_by('name')
    new_place_form = NewPlaceForm()
    #render = combining templates and data together
    return render(request, 'travel_wishlist/wishlist.html', {'places':places, 'new_place_form': new_place_form})

@login_required
def delete_place(request, place_id):
    '''
    Gives user the option to delete entered names from the place list and visited list
    '''
    place = get_object_or_404(Place, id=place_id)
    if place.user == request.user:
        place.delete()
        return redirect('place_list')
    else:
        return HttpResponseForbidden

@login_required
def places_visited(request):
    '''
    Creates the page that saves the places with the visited value of True
    '''

    visited = Place.objects.filter(visited = True)
    return render(request,'travel_wishlist/visited.html', {'visited': visited})

@login_required
def place_details(request, place_id):
    '''
    Creates the page to show: place name, notes on the place, and date visited details
        -also gives the option to delete the entry
    '''
    message = messages
    place = get_object_or_404(Place, id=place_id)
    

    #Does this place belong to the current user?
    if place.user != request.user:
        return HttpResponseForbidden()

    # is this a GET(show data + form) or a POST request(Update place object )?

     #if POST request, validate data form and update
    if request.method == 'POST':
        form = TripReviewForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            message.info(request, 'Trip information updated')
        else:
            message.error(request, form.errors)
        
        return redirect('place_details', place_id=splace_id)
        
    else:
        if place.visited:
            review_form = TripReviewForm(instance=place)
            return render(request, 'travel_wishlist/place_detail.html', {'place':place, 'review_form':review_form })
        else: 
            return render(request, 'travel_wishlist/place_detail.html', {'place':place})
     #if GET requ  est, show place info and form

   


@login_required
def place_was_visited(request, place_id):
    '''
    once the unvisited item is marked as True, this function sends the location to visited places, and removes the entry from place_list
    '''
    if request.method == 'POST':
        place = get_object_or_404(Place, id=place_id)
        if place.user == request.user:
            place.visited = True
            place.save()

        #place = Place.objects.get(id=place_id)



    return redirect('place_list')


def about(request):
    '''
    Create the about page 
    '''
    author = 'Stewart'
    about = 'This website is for listing desired travel destinations and being able to mark them as visited'
    return render(request, 'travel_wishlist/about.html', {'author':author, 'about': about})

