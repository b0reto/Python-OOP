from project.beverage.hot_beverage import HotBeverage


class Cofee(HotBeverage):
    MILILITERS = 50
    PRICE = 3.5
    CAFFEINE = float

    def __init__(self, name, price, mililiters):
        super().__init__(name, price, mililiters)

    @property
    def mililiters(self):
        return self.MILILITERS

    @property
    def price(self):
        return self.PRICE

    @property
    def caffeine(self):
        return self.CAFFEINE
