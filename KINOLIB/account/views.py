from django.shortcuts import render

def showAccount(request):
    context = {                # инфа для заполения страницы ( может обращаться к ключам словаря )
        'title': 'KINOLIB - Главная',
        'content': "Библиотека фильмов и книг KINOLIB <3"

    }

    return render(request, 'acc.html', context)