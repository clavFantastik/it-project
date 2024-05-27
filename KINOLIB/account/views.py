from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.models import Product


def showFavorite(request):
    favorites = Product.objects.all()
    res = []
    for favorite in favorites:
        if favorite.users.filter(id=request.user.id).exists():
            res.append(favorite)

    print(res)
    return render(request, "favorite.html", {"favorites": res})
