from django.shortcuts import render
from home.models import Product
from .models import Message

def ShowAuthHome(request, id):
    if request.method == 'POST':
        if request.POST.get('message') and not Message.objects.filter(description=request.POST.get('message')).exists():
            Message.objects.create(title=request.user.username, description=request.POST.get('message'), product=request.POST.get('product'))

    return render(request, 'film.html', {'product': Product.objects.get(id=str(id)), 'messages': Message.objects.all(), 'str_prod': str(id)})

