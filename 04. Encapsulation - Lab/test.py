class Person:
    def __init__(self, name, age: int):
        self.name = name
        self.age = age


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise Exception('Age cannot be less or equal to 0')

        self.__age = value


p1 = Person('George', 23)
print(p1.age)
p1.age = 66
print(p1.age)
print(p1)