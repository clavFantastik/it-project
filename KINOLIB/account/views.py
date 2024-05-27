from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.models import Product
from .forms import UserEditForm


def showInfo(request):
    if request.method == 'POST' and request.POST.get('id') and not User.objects.filter(username=request.POST.get('username')).exists():
        user = User.objects.get(pk=request.POST.get('id'))
        form = UserEditForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('/profile/info')

    return render(request, 'info.html')


def showFavorite(request):
    favorites = Product.objects.all()
    res = []
    for favorite in favorites:
        if favorite.users.filter(id=request.user.id).exists():
            res.append(favorite)

    print(res)
    return render(request, 'favorite.html', {'favorites': res})



