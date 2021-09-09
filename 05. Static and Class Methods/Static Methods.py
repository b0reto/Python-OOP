class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_adult(age):
        return age >= 18

print(Person.is_adult(11))
girl = Person('Sara')
print(girl.is_adult(22))