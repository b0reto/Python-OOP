from abc import ABC

from project.vehicle import Vehicle


class Truck(Vehicle, ABC):
    AIR_CONDITIONER_FUEL_CONSUMTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        total_consumption = 0
        if (self.fuel_consumption + Truck.AIR_CONDITIONER_FUEL_CONSUMTION) * distance <= self.fuel_quantity:
            total_consumption = (self.fuel_consumption + Truck.AIR_CONDITIONER_FUEL_CONSUMTION) * distance
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95

