from django.conf import settings
from decimal import Decimal
from shop.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Initialising cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def __iter__(self):
        """
        Sorting out products in cart and receiving products from db
        """
        product_ids = self.cart.keys()
        #receiving products and addding them into cart
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Counts products in cart
        """
        return len(self.cart)

    def add(self, product, quantity=1):
        """
        Adding product into cart and updating its quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity                             
        self.save()

    def remove_one(self, product, quantity=1):
        """Removes one product instance from cart"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        self.cart[product_id]['quantity'] -= quantity                             
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """
        Delete product
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        """
        receiving total price
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Clears cart in session
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_quantity(self):
        total_quantity = [item['quantity'] for item in self.cart.values()]
        return sum(total_quantity)