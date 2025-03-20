from django.urls import path
from .views import usersRegisterView, usersProfileView, usersLogoutView

from django.contrib.auth import views

urlpatterns = [
    path("register", usersRegisterView, name="usersRegister"),
    path("login", views.LoginView.as_view(template_name="users/login.html"), name="usersLogin"),
    path("logout", usersLogoutView, name="usersLogout"),
    path("profile", usersProfileView, name="usersProfile"),
]

