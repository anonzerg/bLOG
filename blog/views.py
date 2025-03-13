from django.shortcuts import render
from .models import Post

# Create your views here.

def blogHomeView(request):
    context = {
        "title": "Home",
        "posts": Post.objects.all(),
    }
    return render(request, "blog/home.html", context)

def blogAboutView(request):
    context = {
        "title": "About",
    }
    return render(request, "blog/about.html", context)

