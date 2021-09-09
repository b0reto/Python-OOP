class dictionary_iter():
    def init(self, d) -> None:
        self.data = d
        self.data = iter(self.data.items())

    def iter(self):
        self.data = iter(self.data.items())
        return self

    def next(self):
        return next(self.__data)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
