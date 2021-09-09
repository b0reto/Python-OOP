# from Problem_02_Zoo.lizard import Lizard
# from Problem_02_Zoo.mammal import Mammal
#
# mammal = Mammal("Stella")
# print(mammal.__class__.__bases__[0].__name__)
# print(mammal.name)
# print(mammal._Animal__name)
# lizard = Lizard("John")
# print(lizard.__class__.__bases__[0].__name__)
# print(lizard.name)
# print(lizard._Animal__name)
# zero test
from Problem_02_Zoo.animal import Animal
from Problem_02_Zoo.mammal import Mammal
from Problem_02_Zoo.lizard import Lizard
import unittest


class Tests(unittest.TestCase):
   def test(self):
       mammal = Mammal("Stella")
       self.assertEqual(mammal.__class__.__bases__[0].__name__, "Animal")
       self.assertEqual(mammal.name, "Stella")
       lizard = Lizard("John")
       self.assertEqual(lizard.__class__.__bases__[0].__name__, "Reptile")
       self.assertEqual(lizard .name, "John")
       from platform import python_version
       print('python_version()', python_version())

if __name__ == "__main__":
   unittest.main()