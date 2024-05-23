from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView
from django.core.paginator import Paginator

from . import models


class Utilties(TemplateView):
    template_name = "utility/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locations = models.Location.objects.all()
        location_paginator = Paginator(locations, 5)
        page_number = self.request.GET.get('page')
        context['location_object'] = location_paginator.get_page(page_number)

        sector = models.Sector.objects.all()
        sector_paginator = Paginator(sector, 5)
        page_number = self.request.GET.get('page')
        context['sector_object'] = location_paginator.get_page(page_number)

        donor = models.Donor.objects.all()
        donor_paginator = Paginator(donor, 5)
        page_number = self.request.GET.get('page')
        context['donor_object'] = location_paginator.get_page(page_number)

        return context
    
class Locations(ListView):
    model = models.Location

class Donors(ListView):
    model = models.Donor

class Sectors(ListView):
    model = models.Sector
