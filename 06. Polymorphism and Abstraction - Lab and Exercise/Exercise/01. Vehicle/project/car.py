from abc import ABC

from project.vehicle import Vehicle


class Car(Vehicle, ABC):
    AIR_CONDITIONER_FUEL_CONSUMTION = 0.9


    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        drive_consumption = 0
        if (self.fuel_consumption + Car.AIR_CONDITIONER_FUEL_CONSUMTION) * distance <= self.fuel_quantity:
            drive_consumption = (self.fuel_consumption + Car.AIR_CONDITIONER_FUEL_CONSUMTION) * distance
            self.fuel_quantity -= drive_consumption



    def refuel(self, fuel):
        self.fuel_quantity += fuel
