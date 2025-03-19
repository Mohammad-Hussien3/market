from django.contrib import admin
from .models import Item, Category, Order, Package, PackageItem, PointItem, OrderItem, OrderPointItem
# Register your models here.

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Package)
admin.site.register(PackageItem)
admin.site.register(PointItem)
admin.site.register(OrderPointItem)
admin.site.register(OrderItem)
