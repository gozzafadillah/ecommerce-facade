class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product_id, quantity):
        self.items[product_id] = self.items.get(product_id, 0) + quantity

    def remove_item(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id] -= quantity
            if self.items[product_id] <= 0:
                del self.items[product_id]

    def get_items(self):
        return self.items