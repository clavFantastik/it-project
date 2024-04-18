
from django.contrib import admin
from django.urls import path, include
from user_sign import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('home.urls')), # тут поменял с аккаунтом
    path('login/', include('user_sign.urls')),
    path('', include('account.urls')),
    # path('auth_home/', include('auth_home.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('catalog/', include('goods.urls'))
    
]
