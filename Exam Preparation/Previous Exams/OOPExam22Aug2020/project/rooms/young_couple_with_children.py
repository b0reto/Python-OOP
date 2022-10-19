from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        self.members_count = 2 + len(children)
        self.room_cost = 30
        appl = [TV(), Laptop(), Fridge()]
        [appl.extend([TV(), Laptop(), Fridge()]) for el in range(self.members_count - 1)]
        self.appliances = appl
        self.budget = salary_one + salary_two
        super().__init__(family_name, self.budget, self.members_count)
        self.children = children

