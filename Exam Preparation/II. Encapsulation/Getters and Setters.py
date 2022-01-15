class Car:
    def __init__(self):
        self.max_speed = 200

    def drive(self):
        print('driving max speed ' + str(self.max_speed))

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        self.__max_speed = value


red_car = Car()
red_car.drive()  # driving max speed 200
red_car.max_speed = 10  # changes the speed
red_car.drive()  # driving max speed 10
