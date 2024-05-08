from django.contrib import admin
from .models import LocationModel, DonorModel, SectorModel

admin.site.register(LocationModel)
admin.site.register(DonorModel)
admin.site.register(SectorModel)
