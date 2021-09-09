class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")

        res = [ord(el) + other for el in self.text]
        for each_entry in range(len(res)):
            if res[each_entry] < 32:
                res[each_entry] += 95
            elif res[each_entry] > 126:
                res[each_entry] -= 95
        return_value = ""
        for el in range(len(res)):
            return_value += chr(res[el])
        return return_value


some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))

example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))
