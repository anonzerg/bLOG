from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blogHomeView(request):
    return HttpResponse("<h1>Home</h1>")

def blogAboutView(request):
    return HttpResponse("<h1>About</h1>")

