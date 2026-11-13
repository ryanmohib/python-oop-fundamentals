
from product import Product


class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.__items.append(product)
            print(f"{product.name} added to cart!")
        else:
            print("Invalid product!")

    def remove_product(self, product):
        if product in self.__items:
            self.__items.remove(product)
            print(f"{product.name} removed from cart!")
        else:
            print("Product not found!")

    def calculate_total(self):
        return sum(product.price for product in self.__items)

    def display_cart(self):
        if not self.__items:
            print("Your cart is empty!")
            return

        print("\n--- Shopping Cart ---")

        for product in self.__items:
            product.display_info()

        print(f"Total: {self.calculate_total()}")
