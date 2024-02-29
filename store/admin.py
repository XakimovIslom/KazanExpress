from django.contrib import admin

from store.models import Product, Shop, Category, Role, Photo


class CategoryTestAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title', 'parent__title')
    list_display = ('id', 'title', 'parent')
    list_display_links = ('id', 'title',)


class ShopTestAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title')
    list_display_links = ('id', 'title',)

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return [field.name for field in obj._meta.fields if field.name != 'shop_id']
    #     else:
    #         return []

    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


class ProductTestAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title',)
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title',)
    sortable_by = ('price',)
    list_filter = ('is_active',)


admin.site.register(Shop, ShopTestAdmin)
admin.site.register(Photo)
admin.site.register(Role)
admin.site.register(Product, ProductTestAdmin)
admin.site.register(Category, CategoryTestAdmin)
