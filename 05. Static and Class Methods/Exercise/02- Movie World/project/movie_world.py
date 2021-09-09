from project.customer import Customer

from project.dvd import DVD




class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if self.customers < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if self.dvds < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        pass

