from django.urls import path
from .views import Webhook, HomePage, GetUserPhoto, GetUserPoints

urlpatterns = [
    path('webhook/', Webhook.as_view(), name="webhook"),
    path('homepage/', HomePage.as_view(), name='homepage'),
    path('getphoto/<int:user_id>/', GetUserPhoto.as_view(), name='getphoto'),
    path('getpoints/<int:user_id>/', GetUserPoints.as_view(), name='getuserpoints')
]
