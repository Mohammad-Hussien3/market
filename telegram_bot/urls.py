from django.urls import path
from .views import Webhook, HomePage, GetUserPhotoAndPoints

urlpatterns = [
    path('webhook/', Webhook.as_view(), name="webhook"),
    path('homepage/', HomePage.as_view(), name='homepage'),
    path('getphotoandpoints/<int:user_id>/', GetUserPhotoAndPoints.as_view(), name='getphotoandpoints'),
]
