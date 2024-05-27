
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('account/', include('user_sign.urls')),
    path('page/<int:id>/', include('auth_home.urls')),
    path('profile/', include('account.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
