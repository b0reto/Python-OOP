class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.start = -1
        self.stop = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number not in range(len(self.sequence)+1):
            substract = self.number - len(self.sequence)
            self.number = self.number - substract
            self.start = -1

        self.start += 1
        if self.stop == 0:
            raise StopIteration
        self.stop -= 1
        if self.start not in range(len(self.sequence)):
            self.start = 0
        return self.sequence[self.start]


result = sequence_repeat('abc', 7)
for item in result:
    print(item, end='')
