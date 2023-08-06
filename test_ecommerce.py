import unittest
from ecommerce import EcommerceFacade

class TestEcommerceFacade(unittest.TestCase):
    def setUp(self):
        self.ecommerce = EcommerceFacade()

    def test_add_product_success(self):
        self.ecommerce.add_product('P001', 'Shirt', 25.0)
        self.assertEqual(self.ecommerce.product_catalog.get_product('P001')['name'], 'Shirt')

    def test_add_item_to_cart_success(self):
        self.ecommerce.add_product('P001', 'Shirt', 25.0)
        self.ecommerce.add_item_to_cart('P001', 2)
        items = self.ecommerce.shopping_cart.get_items()
        self.assertEqual(items.get('P001'), 2)

    def test_remove_item_from_cart_success(self):
        self.ecommerce.add_product('P001', 'Shirt', 25.0)
        self.ecommerce.add_item_to_cart('P001', 2)
        self.ecommerce.remove_item_from_cart('P001', 1)
        items = self.ecommerce.shopping_cart.get_items()
        self.assertEqual(items.get('P001'), 1)

    def test_checkout_success(self):
        self.ecommerce.add_product('P001', 'Shirt', 25.0)
        self.ecommerce.add_product('P002', 'Jeans', 40.0)
        self.ecommerce.add_item_to_cart('P001', 2)
        self.ecommerce.add_item_to_cart('P002', 1)
        self.ecommerce.checkout()

    def test_checkout_failure(self):
        self.ecommerce.add_product('P001', 'Shirt', 25.0)
        self.ecommerce.add_product('P002', 'Jeans', 40.0)
        self.ecommerce.add_item_to_cart('P001', 2)
        self.ecommerce.add_item_to_cart('P002', 1)
        self.ecommerce.checkout()
        # Trying to checkout again with insufficient funds
        self.ecommerce.checkout()

if __name__ == "__main__":
    unittest.main()
