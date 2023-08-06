from ecommerce import EcommerceFacade

def main():
    ecommerce = EcommerceFacade()

    # Adding products to the product catalog
    ecommerce.add_product('P001', 'Shirt', 25.0)
    ecommerce.add_product('P002', 'Jeans', 40.0)
    ecommerce.add_product('P003', 'Shoes', 30.0)

    # Adding items to the shopping cart
    ecommerce.add_item_to_cart('P001', 2)
    ecommerce.add_item_to_cart('P002', 1)
    ecommerce.add_item_to_cart('P003', 1)

    # Removing items from the shopping cart
    ecommerce.remove_item_from_cart('P001', 1)

    # Checkout
    ecommerce.checkout()

if __name__ == "__main__":
    main()
