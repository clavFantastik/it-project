from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUpPage, name="signup"),
    path("login/", views.LogInPage, name="login"),
    path("logout/", views.LogoutPage, name="logout"),
]
