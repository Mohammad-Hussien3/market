from django.urls import path
from .views import AllItmes

urlpatterns = [
    path('category/<int:id>/', AllItmes.as_view(), name='allitems'),
]
