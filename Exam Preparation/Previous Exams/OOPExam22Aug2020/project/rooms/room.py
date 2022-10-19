class Room:
    def __init__(self, name, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self._expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculcate_expenses(self, *args):
        for i in args:
            for j in i:
                self.expenses += j.get_monthly_expense()
