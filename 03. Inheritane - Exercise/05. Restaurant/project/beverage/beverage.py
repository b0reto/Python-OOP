from project.product import Product


class Beverage(Product):
    def __init__(self, name, price, mililiters):
        super().__init__(name, price)
        self.mililiters = mililiters
