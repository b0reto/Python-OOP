from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle, ABC):
    AIR_CONDITIONER_FUEL_CONSUMTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)


    def drive(self, distance):
        total_consumption = 0
        if (self.fuel_consumption + Car.AIR_CONDITIONER_FUEL_CONSUMTION) * distance <= self.fuel_quantity:
            total_consumption = (self.fuel_consumption + Car.AIR_CONDITIONER_FUEL_CONSUMTION) * distance
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle, ABC):
    AIR_CONDITIONER_FUEL_CONSUMTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        total_consumption = 0
        if (self.fuel_consumption + Truck.AIR_CONDITIONER_FUEL_CONSUMTION) * distance <= self.fuel_quantity:
            total_consumption = (self.fuel_consumption + Truck.AIR_CONDITIONER_FUEL_CONSUMTION) * distance
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
