from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        self.budget = salary_one + salary_two
        self.members_count = 2
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]

        super(YoungCouple, self).__init__(family_name, self.budget, self.members_count)

