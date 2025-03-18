from django.urls import path
from .views import Webhook, HomePage, GetProfile

urlpatterns = [
    path('webhook/', Webhook.as_view(), name="webhook"),
    path('homepage/', HomePage.as_view(), name='homepage'),
    path('profile/<int:telegramId>/', GetProfile.as_view(), name='profile'),
]
