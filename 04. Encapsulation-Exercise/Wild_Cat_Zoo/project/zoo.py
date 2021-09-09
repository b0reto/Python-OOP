from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget - price > 0:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for ind_worker in self.workers:
            if ind_worker.name == worker_name:
                self.workers.remove(ind_worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for ind_worker in self.workers:
            total_salaries += ind_worker.salary

        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        amount_to_reduce = 0
        for ind_animal in self.animals:
            amount_to_reduce += ind_animal.MONEY_FOR_CARE
        if self.__budget - amount_to_reduce > 0:
            self.__budget -= amount_to_reduce
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        adict = {'Lion': 0, 'Tiger': 0, 'Cheetah': 0}
        for i in range(len(self.animals)):
            adict[self.animals[i].__class__.__name__] += 1

        res = ""
        res += f"You have {len(self.animals)} animals\n"

        for key, value in adict.items():
            res += f"----- {value} {key}s:\n"
            for animal in range(len(self.animals)):
                if self.animals[animal].__class__.__name__ == key:
                    res += f"{self.animals[animal].__repr__()}\n"

        return res.strip()


    def workers_status(self):
        wdict = {'Keeper': 0, 'Caretaker': 0, 'Vet': 0}
        for i in range(len(self.workers)):
            wdict[self.workers[i].__class__.__name__] += 1

        res = ""
        res += f"You have {len(self.workers)} workers\n"

        for key, value in wdict.items():
            res += f"----- {value} {key}s:\n"
            for worker in range(len(self.workers)):
                if self.workers[worker].__class__.__name__ == key:
                    res += f"{self.workers[worker].__repr__()}\n"

        return res.strip()
