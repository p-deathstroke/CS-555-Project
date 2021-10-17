import unittest
from US08 import Family
from US08 import Individual
from US08 import birth_before_marriage_of_parents

class TestApp(unittest.TestCase):
    def test_birth_before_marriage_of_parents(self):
        individual = Individual(_id="I20", birt={'date': "12 nov 2008"})
        family =Family(_id="I21" , marr={'date':"1 feb 2006"}, div= {'date':"5 Mar 2010"}) 
        self.assertTrue(birth_before_marriage_of_parents(family, individual))

        individual = Individual(_id="I20", birt={'date': "1 dec 2010"})
        family =Family(_id="I21" , marr={'date':"15 mar 2009"}, div= {'date':"25 jun 2012"}) 
        self.assertTrue(birth_before_marriage_of_parents(family, individual))

        individual = Individual(_id="I20", birt={'date': "11  dec 2008"})
        family =Family(_id="I21" , marr={'date':"21 may 2007"}, div= {'date':"5 sep 2007"}) 
        self.assertFalse(birth_before_marriage_of_parents(family, individual))

        individual = Individual(_id="I20", birt={'date': "22  dec 2008"})
        family =Family(_id="I21" , marr={'date':"21 may 2004"}, div= {'date':"15 sep 2009"}) 
        self.assertTrue(birth_before_marriage_of_parents(family, individual))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)