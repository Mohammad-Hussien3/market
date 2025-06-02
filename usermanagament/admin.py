from django.contrib import admin
from .models import Profile, Admin
# Register your models here.

admin.site.register(Profile)

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('admin_password', 'sub_admin_password')

    def has_add_permission(self, request):
        return not Admin.objects.exists()

    def changelist_view(self, request, extra_context=None):
        from django.shortcuts import redirect
        obj = Admin.get_instance()
        return redirect(f'/admin/{self.model._meta.app_label}/{self.model._meta.model_name}/{obj.pk}/change/')