from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, name: str, pension_one, pension_two):
        self.members_count = 2
        self.budget = pension_one + pension_two
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove(), TV(), Fridge(), Stove()]
        super().__init__(name, self.budget, self.members_count)

