from django.urls import path
from .views import *

urlpatterns = [
    path('category/<int:id>/<str:item_type>/', CategoryItems.as_view(), name='categoryitems'),
    path('item/<int:id>/', GetItem.as_view(), name='getitem'),
    path('pointitem/<int:id>/', GetPointItem.as_view(), name='getpointitem'),
    path('package/<int:id>/', GetPackage.as_view(), name='getpackage'),
    path('packages/', GetPackages.as_view(), name='getpackages'),
    path('getitems/', AllItems.as_view(), name='allitems'),
    path('getorders/<str:active_type>/', GetOrders.as_view(), name='getorders'),
    path('getorder/<int:id>/', GetOrder.as_view(), name='getorder'),
    path('getpointitems/', GetPointItmes.as_view(), name='getpointitems'),
    path('search/<str:category_type>/<str:text>/', Search.as_view(), name='search'),
    path('searchpackage/<str:text>/', SearchPackage.as_view(), name='search'),
    path('createorder/',CreateOrder.as_view(), name='createOrder'),
    path('categorylist/', CategoryList.as_view(), name='categoryList'),
    path('makeorderdelivery/<int:order_id>/', MakeOrderDelivery.as_view(), name='makeorderdelivery'),
    path('makeorderfinished/<int:order_id>/', MakeOrderFinished.as_view(), name='makeorderfinished'),
    path('getcategory/<int:id>/', GetCategory.as_view(), name='getcategory'),
    path('finishedorders/', GetFinishedOrders.as_view(), name='finishedorders'),

    path('newitem/', CreateItem.as_view(), name='createitem'),
    path('newpointitem/', CreatePointItem.as_view(), name='createpointitem'),
    path('newcategory/', CreateCategory.as_view(), name='createitem'),
    path('newpackage/', CreatePackage.as_view(), name='createpackage'),

    path('deleteitem/<int:id>/', DeleteItem.as_view(), name='deleteitem'),
    path('deletepointitem/<int:id>/', DeletePointItem.as_view(), name='deletepointitem'),
    path('deletecategory/<int:id>/', DeleteCategory.as_view(), name='deletecategory'),
    path('deletepackage/<int:id>/', DeletePackage.as_view(), name='deletepakcage'),
    path('deleteorder/<int:id>/', DeleteOrder.as_view(), name='deleteorder'),

    path('edititem/<int:id>/', UpdateItem.as_view(), name='edititem'),
    path('editpointitem/<int:id>/', UpdatePointItem.as_view(), name='edieditpointitemtitem'),
    path('editcategory/<int:id>/', UpdateCategory.as_view(), name='editcategory'),
    path('editpackage/<int:id>/', UpdatePackage.as_view(), name='editpackage'),
    path('global-points/update/', UpdateGlobalPointsView.as_view(), name='update-global-points'),
]
