class Person:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age


person = Person('Peter', 25)
print(person.name)  # Peter
print(person.age)  # 25
