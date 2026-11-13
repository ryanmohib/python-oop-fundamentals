
class Product:
    def __init__(self, name, price):
        if not name.strip():
            raise ValueError("Product name cannot be empty")

        self.name = name
        self.__price = price

        if price < 0:
            raise ValueError("Price cannot be negative")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")

        self.__price = new_price

    def display_info(self):
        print(f"Product: {self.name} | Price: {self.price}")
