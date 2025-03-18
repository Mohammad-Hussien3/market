from django.urls import path
from .views import *

urlpatterns = [
    path('category/<int:id>/<str:item_type>/', AllItmes.as_view(), name='allitems'),
    path('item/<int:id>/', GetItem.as_view(), name='getitem'),
    path('packages/', GetPackages.as_view(), name='getpackages'),
    path('packageitems/<int:id>/', GetPackagesItems.as_view(), name='package-items'),
    path('getitems/', GetItems.as_view(), name='getitems'),

    path('newitem/', CreateItem.as_view(), name='createitem'),
    path('newcategory/', CreateCategory.as_view(), name='createitem'),
    path('newpackage/', CreatePackage.as_view(), name='createpackage'),
    path('newpackageitem/', CreatePackageItem.as_view(), name='createpackageitem'),

    path('deleteitem/<int:id>/', DeleteItem.as_view(), name='deleteitem'),
    path('deletecategory/<int:id>/', DeleteCategory.as_view(), name='deletecategory'),
    path('deletepackage/<int:id>/', DeletePackage.as_view(), name='deletepakcage'),
    path('deletepackageitem/', DeletePackageItem.as_view(), name='deletepackageitem'),

    path('edititem/<int:id>/', UpdateItem.as_view(), name='edititem'),
    path('editcategory/<int:id>/', UpdateCategory.as_view(), name='editcategory'),
    path('editpackage/<int:id>/', UpdatePackage.as_view(), name='editpackage'),
    path('editpackageitem/', UpdatePackageItem.as_view(), name='editpackageitem'),
]
