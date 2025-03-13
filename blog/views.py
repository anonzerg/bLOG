from django.shortcuts import render

# Create your views here.

def blogHomeView(request):
    context = {
        "title": "Home",
    }
    return render(request, "blog/home.html", context)

def blogAboutView(request):
    context = {
        "title": "About",
    }
    return render(request, "blog/about.html", context)

