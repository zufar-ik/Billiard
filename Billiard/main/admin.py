from django.contrib import admin

from .models import Product, Category


class ProductAdmin(admin.StackedInline):
    model = Product
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductAdmin]
    class Meta:
        model = Product
