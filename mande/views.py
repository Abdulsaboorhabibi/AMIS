from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

# list of all Projects 
class ListProject(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = models.ProjectModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = models.ProjectModel.objects.count()
        context["using"] = models.ProjectModel.objects.filter(overall_Status="C").count()
        context["Processing"] = models.ProjectModel.objects.filter(overall_Status="P").count()
        context["Pendding"] = models.ProjectModel.objects.filter(overall_Status="PN").count()
        return context
    

# detail project 
class DetailProject(DetailView):
    model = models.ProjectModel