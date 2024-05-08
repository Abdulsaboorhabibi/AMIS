from django.urls import path
from django.views.generic import TemplateView


app_name = 'base' 

urlpatterns = [
    path("", TemplateView.as_view(template_name="base/index.html"), name="index" ),
    path("about/", TemplateView.as_view(template_name="base/about.html"), name="about"),
    path("contact/", TemplateView.as_view(template_name="base/contact.html"), name="contact"),
]