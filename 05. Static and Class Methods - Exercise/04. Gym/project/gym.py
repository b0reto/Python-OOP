from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.trainer import Trainer
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    @staticmethod
    def get_object(object_id, class_iterable):
        # TODO: fix this
        return (filter(lambda _: _.id == object_id, class_iterable))[0]

    def subscription_info(self, subscription_id: int):
        current_subscrition = self.get_object(subscription_id, self.subscriptions)
        customer_id = current_subscrition.customer_id
        current_customer = self.get_object(customer_id, self.customers)
        trainer_id = current_subscrition.trainer_id
        current_trainer = self.get_object(trainer_id, self.trainers)
        current_plan = self.get_object(trainer_id, self.plans)
        current_equipment = self.get_object(current_plan.equipment_id, self.equipment)
        return f"{current_subscrition}\n{current_customer}\n{current_trainer}\n{current_equipment}\n{current_plan}"
