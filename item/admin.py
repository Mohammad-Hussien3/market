from django.contrib import admin
from .models import Item, Category, Order, Package, PackageItem
# Register your models here.

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Package)
admin.site.register(PackageItem)
