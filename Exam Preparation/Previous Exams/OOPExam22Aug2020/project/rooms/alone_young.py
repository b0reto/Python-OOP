from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

    def __init__(self, name, salary):
        self.members_count = 1
        self.budget = salary
        self.room_cost = 10
        self.appliances = [TV()]
        super().__init__(name, salary, self.members_count)
