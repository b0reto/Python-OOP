class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25
    # fuel_consumption = float
    # fuel = float
    # horse_power = int

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        # за да може да работи с default_fuel_consumption
        # за всеки клас, използваме self
        # тази думичка замества името на конкретния клас
        # така взимаме клас атрибута на класа, в който сме


    def drive(self, kilometers):
        if self.fuel - kilometers * self.fuel_consumption >= 0:
            self.fuel -= kilometers * self.fuel_consumption



vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
# vehicle.drive(100)
# print(vehicle.fuel)
# # family_car = FamilyCar(150, 150)
# # family_car.drive(50)
# # print(family_car.fuel)
# # family_car.drive(50)
# # print(family_car.fuel)
# # print(family_car.__class__.__bases__[0].__name__)
#
