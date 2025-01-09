from django.contrib import admin

from .models import Category, Product, File


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enabled', 'created_time']
    list_filter = ['is_enabled', 'parent']
    search_fields = ['title']


class FileInline(admin.StackedInline):
    model = File
    fields = ['title', 'file', 'is_enabled']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [FileInline]
    list_display = ['title', 'is_enabled', 'created_time']
    filter_horizontal = ['categories']
    list_filter = ['is_enabled']
    search_fields = ['title']
