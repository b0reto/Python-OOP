from project.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price, mililiters):
        super().__init__(name, price, mililiters)