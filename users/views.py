from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout

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
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f"account info has been updated!")
            return redirect("usersProfile")
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"title": "profile", "user_update_form": user_update_form, "profile_update_form": profile_update_form}
    return render(request, "users/profile.html", context)

def usersLogoutView(request):
    logout(request)
    context = {"title": "logout"}
    return render(request, "users/logout.html", context)

