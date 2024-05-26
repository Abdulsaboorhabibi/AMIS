from django.urls import path
from . import views

app_name = "mande"

urlpatterns = [
    path("", views.ListProject.as_view(), name="index"),
    path("detail/<str:slug>", views.DetailProject.as_view(), name="project-details"),
    path("create/", views.CreateProject.as_view(), name="create-project"),
]
