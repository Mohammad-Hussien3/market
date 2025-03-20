from django.urls import path
from .views import Webhook, HomePage, GetPoints

urlpatterns = [
    path('webhook/', Webhook.as_view(), name="webhook"),
    path('homepage/', HomePage.as_view(), name='homepage'),
    path('getpoints/<int:telegram_id>/', GetPoints.as_view(), name='getpoints'),
]
