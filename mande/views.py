from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from . import models
from . import project_form

# list of all Projects 
class ListProject(LoginRequiredMixin, ListView):
    paginate_by = 1
    model = models.Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = models.Project.objects.count()
        context["using"] = models.Project.objects.filter(overall_Status="C").count()
        context["Processing"] = models.Project.objects.filter(overall_Status="P").count()
        context["Pendding"] = models.Project.objects.filter(overall_Status="PN").count()
        return context
    

# detail project 
class DetailProject(DetailView):
    model = models.Project
    paginate = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        monitors = models.MonitorProject.objects.filter(project=project)
        paginator = Paginator(monitors, self.paginate)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        return context
    
# create new project view
class CreateProject(CreateView):
    template_name = "mande/create_project.html"
    model = models.Project
    #fields = "__all__"
    form_class = project_form.ProjectForm
    success_url = '/mande/'

    def form_valid(self, form):
        # form
        return super().form_valid(form)
    