from django.urls import path
from .views import AllItmes, GetItem

urlpatterns = [
    path('category/<int:id>/<str:item_type>/', AllItmes.as_view(), name='allitems'),
    path('item/<int:id>/', GetItem.as_view(), name='getItem'),
]
