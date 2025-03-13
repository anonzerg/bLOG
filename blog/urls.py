from django.urls import path
from .views import blogHomeView, blogAboutView

urlpatterns = [
    path("", blogHomeView, name="blogHome"),
    path("about/", blogAboutView, name="blogAbout"),
]

