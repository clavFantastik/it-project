from django.shortcuts import render

from goods.models import Products

def catalog(request):

    goods = Products.objects.all()

    context = {  # инфа для заполения страницы ( обращаться к ключам словаря )
        'title': 'KINOLIB - Главная',
        'content': "Библиотека фильмов и книг KINOLIB <3",
        'goods': goods

    }
    return render(request, 'catalog.html', context)

def product(request, product_id):
    product = Products.objects.get(id=product_id)   # получаем инфу из бд по id

    context = {
        'product': product
    }

    return render(request, 'product.html', context=context)
