from django.shortcuts import render, redirect
from .models import Product
import requests
from django.contrib.auth.models import User
from imdb import IMDb
from deep_translator import GoogleTranslator
import random


def checkFavorite(user, elem):
    if elem.users.filter(id=user.id).exists():
        return True

    return False


def showHomePage(request):

    if not request.user.is_authenticated:
        return render(request, 'main.html', {'products': Product.objects.all()})

    return render(request, 'main_auth.html', {'products': Product.objects.all()})


def addFavorite(request, id):
    if Product.objects.get(id=id).users.filter(id=request.user.id).exists():
        Product.objects.get(id=id).users.remove(request.user)
    else:
        Product.objects.get(id=id).users.add(request.user)

    return redirect('/')





