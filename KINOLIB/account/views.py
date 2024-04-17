from django.shortcuts import render

def showAccount(request):
    context = {                # инфа для заполения страницы ( может обращаться к ключам словаря )
        'title': 'Home',
        'content': 'Страничка товара',
        'lol': True
    }

    return render(request, 'account.html', context)