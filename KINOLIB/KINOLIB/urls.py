
from django.contrib import admin
from django.urls import path, include
from user_sign import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login/', include('user_sign.urls')),
    # path('account/', include('account.urls')),
    # path('auth_home/', include('auth_home.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    
]
