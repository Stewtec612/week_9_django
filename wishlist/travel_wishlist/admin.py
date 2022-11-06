from django.contrib import admin
from .models import Place

#Register made model to admin
admin.site.register(Place)
#Create super user account to be able to access admin site
