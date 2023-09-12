from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator
from web.models import Product
from django.http import HttpRequest
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # Валідатор для номера телефону
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='Phone number must be entered in the format: "+380.........". Up to 15 digits allowed.'
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(validators=[phone_regex], max_length=17)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


@receiver(pre_save, sender=Order)
def populate_user_info(sender, instance, **kwargs):
    request = HttpRequest()
    if instance.user_id and instance.user_id is not None:
        instance.user = User.objects.get(id=instance.user_id)
    else:
        instance.user = None


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return 'OrderItem {}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
