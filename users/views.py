from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def usersRegisterView(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"User acount has been created!")
            return redirect("usersLogin")
    else:
        form = UserRegisterForm()
        context = {"form": form, "title": "register"}
    return render(request, "users/register.html", context)

