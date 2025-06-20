from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', include('telegram_bot.urls')),
    path('', include('item.urls')),
    path('', include('usermanagament.urls')),
]