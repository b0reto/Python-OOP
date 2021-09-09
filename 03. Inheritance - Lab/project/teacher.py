from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):
    def teach(self):
        Person.__init__(self)
        Employee.__init__(self)
        return 'teaching...'
