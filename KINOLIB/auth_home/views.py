from django.shortcuts import render
from home.models import Product

def ShowAuthHome(request, id):


    return render(request, 'film.html', {'product': Product.objects.get(id = str(id))})