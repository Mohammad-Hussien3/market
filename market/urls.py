from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', include('telegram_bot.urls')),
    path('', include('item.urls')),
]
