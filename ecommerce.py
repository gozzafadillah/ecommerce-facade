from product_catalog import ProductCatalog
from shopping_chart import ShoppingCart
from payment_gateaway import PaymentGateway

class EcommerceFacade:
    def __init__(self):
        self.product_catalog = ProductCatalog()
        self.shopping_cart = ShoppingCart()
        self.payment_gateway = PaymentGateway()

    def add_product(self, product_id, name, price):
        self.product_catalog.add_product(product_id, name, price)

    def add_item_to_cart(self, product_id, quantity):
        product = self.product_catalog.get_product(product_id)
        if product:
            self.shopping_cart.add_item(product_id, quantity)

    def remove_item_from_cart(self, product_id, quantity):
        self.shopping_cart.remove_item(product_id, quantity)

    def checkout(self):
        total_amount = 0
        items = self.shopping_cart.get_items()

        for product_id, quantity in items.items():
            product = self.product_catalog.get_product(product_id)
            if product:
                total_amount += product['price'] * quantity

        success = self.payment_gateway.process_payment(total_amount)

        if success:
            print("Checkout successful. Your order has been placed.")
            self.shopping_cart = ShoppingCart()
        else:
            print("Checkout failed. Please try again.")
