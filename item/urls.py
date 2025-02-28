from django.urls import path
from .views import AllItmes, GetItem, GetPackages, GetPackagesItems, GetItems

urlpatterns = [
    path('category/<int:id>/<str:item_type>/', AllItmes.as_view(), name='allitems'),
    path('item/<int:id>/', GetItem.as_view(), name='getitem'),
    path('packages/', GetPackages.as_view(), name='getpackages'),
    path('packageitems/<int:id>/', GetPackagesItems.as_view(), name='package-items'),
    path('getitems/', GetItems.as_view(), name='getitems'),
]
