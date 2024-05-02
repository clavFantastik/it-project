from django.urls import path
from . import views

urlpatterns = [
    path("", views.ShowUserSign, name="login"),
    path("authorized/", views.AuthorizedPage, name="authorized"),
    path("example/", views.FilmPage, name="film"),
    path("login/example/", views.FilmPage, name="login_film"),
]
