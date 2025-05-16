from django.urls import path
from .views import *

urlpatterns = [
    path('category/<int:id>/<str:item_type>/', CategoryItems.as_view(), name='categoryitems'),
    path('item/<int:id>/', GetItem.as_view(), name='getitem'),
    path('pointitem/<int:id>/', GetPointItem.as_view(), name='getpointitem'),
    path('package/<int:id>/', GetPackage.as_view(), name='getpackage'),
    path('packages/', GetPackages.as_view(), name='getpackages'),
    path('getitems/', AllItems.as_view(), name='allitems'),
    path('getorders/<int:telegram_id>/<str:status>/', GetOrders.as_view(), name='getorders'),
    path('getpointitems/', GetPointItmes.as_view(), name='getpointitems'),
    path('search/<str:category_type>/<str:text>/', Search.as_view(), name='search'),

    path('newitem/', CreateItem.as_view(), name='createitem'),
    path('newcategory/', CreateCategory.as_view(), name='createitem'),
    path('newpackage/', CreatePackage.as_view(), name='createpackage'),

    path('deleteitem/<int:id>/', DeleteItem.as_view(), name='deleteitem'),
    path('deletecategory/<int:id>/', DeleteCategory.as_view(), name='deletecategory'),
    path('deletepackage/<int:id>/', DeletePackage.as_view(), name='deletepakcage'),

    path('edititem/<int:id>/', UpdateItem.as_view(), name='edititem'),
    path('editcategory/<int:id>/', UpdateCategory.as_view(), name='editcategory'),
    path('editpackage/<int:id>/', UpdatePackage.as_view(), name='editpackage'),
]
