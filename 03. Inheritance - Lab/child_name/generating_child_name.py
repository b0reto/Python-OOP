class Father:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Mother(Father):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


class Child(Father):
    def child_name(self, first_name, second_name: Father, last_name):
        super().__init__(first_name, last_name)
        second_name = second_name.first_name + 'ov'
        full_name = first_name + second_name + last_name
        return full_name


f = Father('Stefan', 'Dundakov')
m = Mother('Petrana', 'Hristova')
c = Child('Boris', 'Dundakov')
print(c.child_name('Boris', 'Stefan', 'Dundakov'))
