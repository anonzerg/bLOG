from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.

def usersRegisterView(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} account has been created!")
            return redirect("usersLogin")
    else:
        form = UserRegisterForm()
        context = {"form": form, "title": "register"}
    return render(request, "users/register.html", context)

@login_required
def usersProfileView(request):
    context = {"title": "profile"}
    return render(request, "users/profile.html", context)

