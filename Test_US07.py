import unittest

from US07 import Individual
from US07 import less_than_150

class TestApp(unittest.TestCase):
    def test_less_than_150(self):
        individual = Individual(birt={'date': "20 Mar 1985"})
        individual.deat = {'date': "15 Aug 2008"}
        self.assertTrue(less_than_150(individual))

        individual = Individual(birt={'date': "15 JAN 2000"})
        self.assertTrue(less_than_150(individual))

        individual = Individual(birt={'date': "15 Feb 2012"})
        individual.deat = {'date': "21 JAN 2000"}
        self.assertFalse(less_than_150(individual))

        individual = Individual(birt={'date': "15 JAN 1500"})
        self.assertFalse(less_than_150(individual))

        individual = Individual(birt={'date': "15 JAN 2006"})
        individual.deat = {'date': "15 JAN 1200"}
        self.assertFalse(less_than_150(individual))

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)