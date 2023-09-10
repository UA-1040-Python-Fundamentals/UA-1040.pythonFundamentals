from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ("name", )
        verbose_name = _('category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('web:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)

    name = models.CharField(max_length=150, db_index=True, verbose_name=_('name'))
    slug = models.CharField(max_length=150, db_index=True, unique=True, verbose_name=_('slug'))
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True, verbose_name=_('image'))
    description = models.TextField(max_length=1000, blank=True, verbose_name=_('description'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'))
    weight = models.IntegerField(default=1, verbose_name=_('weight'))
    weight_unit = models.CharField(max_length=20, choices=[
        ('kg', 'kg'),
        ('g', 'g'),
        ('pcs', 'pcs'),
        ], verbose_name=_('weight_unit'), default='kg')
    available = models.BooleanField(default=True, verbose_name=_('available'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    uploaded = models.DateTimeField(auto_now=True, verbose_name=_('uploaded'))

    class Meta:
        ordering = ("name", )
        verbose_name = _('product')
        verbose_name_plural = _('Products')
        index_together = (("id", "slug"), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('web:product_detail', args=[self.id, self.slug])

