from modeltranslation.translator import register, TranslationOptions
from .models import Product, Category


@register(Product)
class ProductsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

