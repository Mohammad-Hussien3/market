from django.urls import path
from .views import AllItmes, GetItem, GetPackages, GetPackagesItems, GetItems, CreateItem, CreateCategory, DeleteCategory, DeleteItem, UpdateItem, UpdateCategory

urlpatterns = [
    path('category/<int:id>/<str:item_type>/', AllItmes.as_view(), name='allitems'),
    path('item/<int:id>/', GetItem.as_view(), name='getitem'),
    path('packages/', GetPackages.as_view(), name='getpackages'),
    path('packageitems/<int:id>/', GetPackagesItems.as_view(), name='package-items'),
    path('getitems/', GetItems.as_view(), name='getitems'),
    path('newitem/', CreateItem.as_view(), name='createitem'),
    path('newcategory/', CreateCategory.as_view(), name='createitem'),
    path('deleteitem/<int:id>/', DeleteItem.as_view(), name='deleteitem'),
    path('deletecategory/<int:id>/', DeleteCategory.as_view(), name='deletecategory'),
    path('edititem/<int:id>/', UpdateItem.as_view(), name='edititem'),
    path('editcategory/<int:id>/', UpdateCategory.as_view(), name='editcategory'),
]
