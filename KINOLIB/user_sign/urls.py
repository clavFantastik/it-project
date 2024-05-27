from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUpPage, name="signup"),
    path("login/", views.LogInPage, name="login"),
    path("logout/", views.LogoutPage, name="logout"),
    # path("example/", views.FilmPage, name="film"),
    # path("login/example/", views.FilmPage, name="login_film"),
]
