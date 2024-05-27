from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.showInfo, name='info'),
    path('favorite/', views.showFavorite, name='favorite'),
]