class Person:
    def sleep(self):
        return "sleeping..."


class Employee:
    def get_fired(self):
        return "fired..."


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."



first_teacher = Teacher()
print(first_teacher.teach())
print(first_teacher.sleep())
print(first_teacher.get_fired())