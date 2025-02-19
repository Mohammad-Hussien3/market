from django.urls import path
from .views import Webhook, HomePage

urlpatterns = [
    path('webhook/', Webhook.as_view(), name="webhook"),
    path('homepage/', HomePage.as_view(), name='homepage'),
]
