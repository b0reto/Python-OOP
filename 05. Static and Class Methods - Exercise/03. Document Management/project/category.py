class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def edit(self, name):
        self.name = name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"