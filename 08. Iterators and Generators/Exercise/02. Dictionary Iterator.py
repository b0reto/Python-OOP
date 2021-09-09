class dictionary_iter:
    def __init__(self, mydict: {}):
        self.start_index = 0
        self.mydict = mydict

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index == len(self.mydict):
            raise StopIteration
        self.start_index += 1
        res = []
        c = 0
        for key, value in self.mydict.items():
            c += 1
            res.append(key)
            res.extend(value)
            return tuple(res)

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
#
# test zero
import unittest


class DictionaryIteratorTests(unittest.TestCase):
    def test_zero(self):
        result = dictionary_iter({1: "1", 2: "2"})
        expected = []
        for x in result:
            expected.append(x)
        self.assertEqual(expected, [(1, "1"), (2, "2")])


if __name__ == '__main__':
    unittest.main()
