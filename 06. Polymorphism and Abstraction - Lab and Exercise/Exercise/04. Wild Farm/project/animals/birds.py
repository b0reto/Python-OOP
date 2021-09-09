from project.animals.animal import Animal, Bird
from project.food import Vegetable, Meat, Food, Fruit, Seed


class Owl(Bird):
    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Meat":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.25


class Hen(Bird):
    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.35