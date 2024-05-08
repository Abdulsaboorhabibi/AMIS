from django.urls import path 
from . import views

app_name = 'mande'

urlpatterns = [
    path("", views.ListProject.as_view(), name="index_mande" ),
    path("detail/<str:slug>", views.DetailProject.as_view(), name="project-details"),
]