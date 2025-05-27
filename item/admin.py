from django.contrib import admin
from .models import Item, Category, Order, Package, PointItem, OrderItem, OrderPointItem, OrderPackage, GlobalPoints
# Register your models here.

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Package)
admin.site.register(PointItem)
admin.site.register(OrderPointItem)
admin.site.register(OrderItem)
admin.site.register(OrderPackage)


@admin.register(GlobalPoints)
class GlobalPointsAdmin(admin.ModelAdmin):
    list_display = ('referral_points', 'purchase_points', 'referral_purchase_points')

    def has_add_permission(self, request):
        return not GlobalPoints.objects.exists()

    def changelist_view(self, request, extra_context=None):
        from django.shortcuts import redirect
        obj = GlobalPoints.get_instance()
        return redirect(f'/admin/{self.model._meta.app_label}/{self.model._meta.model_name}/{obj.pk}/change/')