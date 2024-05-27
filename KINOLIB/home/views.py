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


def movies_data():
    # Создание объекта IMDb
    ia = IMDb()

    # Список всех фильмов
    movies = [
        ia.get_movie("0068646"),
        ia.get_movie("0111161"),
        ia.get_movie("0468569"),
        ia.get_movie("0071562"),
        ia.get_movie("0050083"),
        ia.get_movie("0108052"),
        ia.get_movie("0167260"),
        ia.get_movie("0110912"),
        ia.get_movie("0120737"),
        ia.get_movie("0060196"),
        ia.get_movie("0109830"),
        ia.get_movie("0167261"),
        ia.get_movie("0137523"),
        ia.get_movie("1375666"),
        ia.get_movie("0133093"),
        ia.get_movie("0099685"),
        ia.get_movie("0073486"),
        ia.get_movie("0114369"),
        ia.get_movie("0816692"),
    ]

    # Создание списка для хранения информации о фильмах
    movies_info = []

    # Инициализация переводчика
    translator = GoogleTranslator(source="en", target="ru")

    # Получение информации о каждом фильме
    for movie in movies:
        movie_id = movie.movieID
        detailed_movie = ia.get_movie(movie_id)

        # Извлечение нужной информации
        title = detailed_movie.get("title", "Нет заголовка")
        plot = detailed_movie.get("plot outline", "Нет описания")
        rating = detailed_movie.get("rating", "Нет рейтинга")
        cover_url = detailed_movie.get("cover url", "Нет изображения")
        year = detailed_movie.get("year", "Нет года выпуска")

        # Перевод на русский язык
        title_ru = (
            translator.translate(title) if title != "Нет заголовка" else "Нет заголовка"
        )
        plot_ru = (
            translator.translate(plot) if plot != "Нет описания" else "Нет описания"
        )

        # Добавление информации о фильме в список
        movies_info.append(
            {
                "title": title_ru,
                "plot": plot_ru,
                "rating": rating,
                "year": year,
                "cover_url": cover_url,
            }
        )

    return movies_info


def fetch_and_display_books():
    num_books = 20
    api_key = "AIzaSyDkn5act0Z-B-5-o-apeZXLlc_hjQF_cmg"
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": "subject:fiction",  # Поиск художественной литературы
        "langRestrict": "ru",  # Ограничение языка книг русским
        "maxResults": 40,  # Запрашиваем больше результатов за один раз
        "key": api_key,
    }
    start_index = 0
    filtered_books = []

    while len(filtered_books) < num_books:
        params["startIndex"] = start_index
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        books_info = data.get("items", [])

        for book in books_info:
            volume_info = book.get("volumeInfo", {})
            rating = volume_info.get("averageRating")

            if rating:  # Фильтруем книги только с известным рейтингом
                title = volume_info.get("title", "Нет заголовка")
                authors = volume_info.get("authors", [])
                author = ", ".join(authors) if authors else "Нет автора"
                description = volume_info.get("description", "Нет описания")
                cover_url = volume_info.get("imageLinks", {}).get(
                    "thumbnail", "Нет изображения"
                )
                published_date = volume_info.get(
                    "publishedDate", "Нет данных о годе издания"
                )

                book_info = {
                    "title": title,
                    "author": author,
                    "rating": rating,
                    "description": description,
                    "cover_url": cover_url,
                    "published_date": published_date,
                }

                filtered_books.append(book_info)

            if len(filtered_books) >= num_books:
                break

        start_index += 40

        if not books_info:
            break

    return filtered_books[:num_books]



def reload(request):
    # for i, info in enumerate(movies_data()):
    #     Product.objects.create(title=info['title'],description=info['plot'], year=int(info['year']), rating=info['rating'], img=info['cover_url'], type='Фильм')

    for i, book in enumerate(fetch_and_display_books()):
        Product.objects.create(title=book['title'], description=book['description'], year=int(book['published_date'].split('-')[0]), rating=book['rating'], img=book['cover_url'], type='Книга')

    return redirect('/')



