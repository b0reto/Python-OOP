from project.animals.animal import Animal, Mammal
from project.food import Food, Meat, Vegetable, Seed, Fruit



class Mouse(Mammal):
    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Fruit" and not food.__class__.__name__ == "Vegetable":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.10


class Dog(Mammal):
    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Meat":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.40


class Cat(Mammal):
    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Meat" and not food.__class__.__name__ == "Vegetable":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.30


class Tiger(Mammal):
    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Meat":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 1.00
