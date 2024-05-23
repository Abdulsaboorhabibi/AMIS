from django.urls import path 
from . import views

app_name = "utility"

urlpatterns = [
    path("", views.Utilties.as_view(), name="index" ),
    path("locations/", views.Locations.as_view(), name="locations" ),
]
