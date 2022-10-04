from django.contrib import admin
from .models import Category, Franchise, Product
from django.utils.safestring import mark_safe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )} #поле slug будет заполняться автоматически в зависимости от поля name

admin.site.register(Category, CategoryAdmin)


class FranchiseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Franchise, FranchiseAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_show', 'name', 'category', 'franchise', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['category', 'franchise', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"
    
    image_show.__name__ = "Image"