from django.urls import path
from .views import AllItmes, GetItem

urlpatterns = [
    path('category/<int:id>/', AllItmes.as_view(), name='allitems'),
    path('item/<int:id>/', GetItem.as_view(), name='getItem'),
]
