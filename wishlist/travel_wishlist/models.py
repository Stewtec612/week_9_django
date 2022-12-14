from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

class Place(models.Model):
    '''The Place model is what the website is modeled around
        -user = ability to create accounts on website that are unique to the individual
        -name = name of website
        -visited = a true/false variable to tag the made place object has been visited or not
        -notes = discriptions for the place created
        -date_visited = keeps track of the date/time when the place object is marked visited
        -photo = image for the place
    '''
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)#Max length of title
    visited = models.BooleanField(default=False)#True/False field
    notes = models.TextField(blank=True, null=True)
    date_visited = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        old_place = Place.objects.filter(id=self.id).first()
        if old_place and old_place.photo:
            if old_place.photo != self.photo:
                self.delete_photo(old_place.photo)

        super().save(*args, **kwargs)

    def delete_photo(self, photo):
        if default_storage.exists(photo.name):
            default_storage.delete(photo.name)


    def __str__(self):#group variables together in a single string
        photo_str = self.photo.url if self.photo else 'no_photo'
        notes_str = self.notes[100:] if self.notes else 'no notes'
        return f'{self.name} visited? {self.visited} on {self.date_visited}. Notes: {notes_str} Photo {photo_str}'#for developer