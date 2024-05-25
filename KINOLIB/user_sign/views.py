from django.shortcuts import render


def FilmPage(request):
    return render(request, "film.html")

def ShowUserSign(request):
    return render(request, "login.html")


def AuthorizedPage(request):
    return render(request, "logIn_2.html")

def ForgotPage(request):
    return render(request, "forgot.html")



