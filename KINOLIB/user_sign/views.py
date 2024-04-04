from django.shortcuts import render


def ShowUserSign(request):
    return render(request, 'login.html')
