from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)#Max length of title
    visited = models.BooleanField(default=False)#True/False field

    def __str__(self):#group variables together in a single string
        return f'{self.name} visited? {self.visited}'#for developer