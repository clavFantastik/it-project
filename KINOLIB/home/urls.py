
from django.urls import path
from . import views
urlpatterns = [
    path('', views.showHomePage, name="home"),
    path('add/<int:id>', views.addFavorite, name="add"),
    path('reload/', views.reload, name="reload")
]
