class ProductCatalog:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price):
        self.products[product_id] = {'name': name, 'price': price}

    def get_product(self, product_id):
        return self.products.get(product_id)

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
