from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, Product
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ["name", "slug", "price", "image_show", "available", "created", "uploaded"]
    list_filter = ["available", "created", "uploaded"]
    list_editable = ["price", "available"]
    prepopulated_fields = {"slug": ("name", )}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='40', height='40' />" .format(obj.image.url))
        return "None"

    image_show.__name__ = "Зображення"
