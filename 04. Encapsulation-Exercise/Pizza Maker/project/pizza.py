from project.topping import Topping
from project.dough import Dough


class Pizza:
    def __init__(self, name, dough: Dough, toppings_capacity):
        self.name = name
        self.dough = [dough.flour_type, dough.baking_technique, dough.weight]
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if not value:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")

        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        if self.toppings_capacity > 0:
            if topping.topping_type not in self.toppings:
                self.toppings[topping.topping_type] = topping.weight
                self.__toppings_capacity -= 1
            else:
                self.toppings[topping.topping_type] += topping.weight
        else:
            raise ValueError("Not enough space for another topping")


    def calculate_total_weight(self):
        res = (self.dough[-1])
        res += sum(self.toppings.values())
        return res