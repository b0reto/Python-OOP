class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = str(name)
        self.age = int(age)
        self.id = int(id)
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({[name for name in self.rented_dvds]})"