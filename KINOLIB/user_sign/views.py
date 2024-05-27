from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import SignInForm
from django.contrib.auth.forms import UserCreationForm


def FilmPage(request):
    return render(request, "film.html")

def SignUpPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')

        if username and password:
            if User.objects.filter(username=username).exists():
               return JsonResponse({'message': 'Пользователь с таким именем уже существует'}, status=400)
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                login(request, user)
                return redirect('/')

    return render(request, "login.html")





def LogInPage(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')


    return render(request, "login_2.html")



def LogoutPage(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/')




