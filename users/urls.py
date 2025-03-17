from django.urls import path
from .views import usersRegisterView

urlpatterns = [
    path("register", usersRegisterView, name="usersRegister"),
]

