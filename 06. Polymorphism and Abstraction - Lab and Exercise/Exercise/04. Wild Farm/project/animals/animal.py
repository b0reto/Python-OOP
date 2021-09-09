from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    def make_sound(self):
        pass


class Bird(Animal):
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight,0)
        self.wing_size = wing_size


class Mammal(Animal):
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight, 0)
        self.living_region = living_region