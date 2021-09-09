class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensor_amount():
        return 1


class MedicalRobot(Robot):
    @staticmethod
    def sensor_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensor_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensor_amount():
        return 12


robots = []
robots.append(Robot('Robo'))
robots.append(MedicalRobot('Da Vinci'))
robots.append(ChefRobot('Moley'))
robots.append(WarRobot('Griffin'))

for robot in robots:
    print(robot.sensor_amount())
