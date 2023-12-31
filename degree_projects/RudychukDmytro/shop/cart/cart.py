from decimal import Decimal
from django.conf import settings
from web.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Ініціалізація кошика
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # зберігаємо порожню корзину в сесії
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Проходим по товарах і отримуємо їх з бази данних
        """
        product_ids = self.cart.keys()
        # отримуємо товари та додаємо їх до кошика
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Рахуємо кількість товарів у кошику
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Додаємо товар до кошика та оновлюємо кількість
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Зберігаємо товар
        self.session.modified = True

    def remove(self, product):
        """
        Видаляємо товар
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        # загальна вартість
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # очищуємо кошик в сесії
        del self.session[settings.CART_SESSION_ID]
        self.save()