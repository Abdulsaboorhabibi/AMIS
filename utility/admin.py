from django.contrib import admin
from .models import Location, Donor, Sector

admin.site.register(Location)
admin.site.register(Donor)
admin.site.register(Sector)
