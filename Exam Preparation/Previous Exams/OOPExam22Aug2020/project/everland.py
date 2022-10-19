class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            room.calculcate_expenses(room.appliances)
            total_consumption += room.expenses + room.room_cost
            child_costs = [child.cost for child in room.children]
            total_consumption += sum(child_costs)

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        res = ""
        for room in self.rooms:
            child_costs = [child.cost for child in room.children]
            monthly_consumption = room.expenses + room.room_cost + sum(child_costs)
            if monthly_consumption > room.budget:
                res += f"{room.family_name} does not have enough budget and must leave the hotel."
                self.rooms.remove(room)
            else:
                room.budget -= monthly_consumption
                res += f"{room.family_name} paid {monthly_consumption:.2f}$ and have {room.budget:.2f}$ left."

        return res

    def status(self):
        res = ""
        guests_count = sum([room.members_count for room in self.rooms])
        res += f"Total population: {guests_count}\n"
        for room in self.rooms:
            child_costs = sum([child.cost for child in room.children])
            res += f"{room.family_name} with {room.members_count} members. Budget {room.budget:.2f}$, Expenses: {room.expenses + child_costs:.2f}$\n "
            if room.children:
                for idx, child in enumerate(room.children):
                    res += f"--- Child {idx + 1} monthly cost: {child.cost:.2f}$\n"

            res += f"--- Appliances monthly cost: {room.expenses:.2f}$\n"

        return res
