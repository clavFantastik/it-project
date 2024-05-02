from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories
def showAccount(request):

    categories = Categories.objects.all()
    context = {                # инфа для заполения страницы ( обращаться к ключам словаря )
        'title': 'KINOLIB - Главная',
        'content': "Библиотека фильмов и книг KINOLIB <3",
        'categories': categories

    }

    return render(request, 'acc.html', context)