import unittest

from Family import Family
from Individual import Individual
from ValidateData import us01_dates_before_current_date, us02_birth_before_marriage, us07_age_less_than_150, us08_birth_before_marriage_of_parents


class TestValidateDataMethod(unittest.TestCase):
    def setUp(self):
        self.individual = Individual("Indiv1")
        self.individual.set_birth_date("12 DEC 1968")
        self.individual.set_death_date("18 JAN 2021")
        self.individual.set_family_id_as_spouse("Fam1")

        self.family = Family("Fam1")
        self.family.set_marriage_date("5 DEC 2001")
        self.family.set_divorce_date("10 JUL 2011")

    def tearDown(self):
        del self.family
        del self.individual

    def test_us01_dates_before_current_date(self):
        self.assertTrue(us01_dates_before_current_date(self.individual.birth_date, "Birth date", self.individual))
        self.assertTrue(us01_dates_before_current_date(self.individual.death_date, "Death date", self.individual))
        self.assertTrue(us01_dates_before_current_date(self.family.marriage_date, "Marriage date", self.family))
        self.assertTrue(us01_dates_before_current_date(self.family.divorce_date, "Divorce date", self.family))

        self.individual.set_birth_date("12 DEC 2068")
        self.assertFalse(us01_dates_before_current_date(self.individual.birth_date, "Birth date", self.individual))

        self.individual.set_death_date("18 JAN 2050")
        self.assertFalse(us01_dates_before_current_date(self.individual.death_date, "Death date", self.individual))

        self.family.set_marriage_date("5 DEC 2060")
        self.assertFalse(us01_dates_before_current_date(self.family.marriage_date, "Marriage date", self.family))

        self.family.set_divorce_date("10 JUL 2065")
        self.assertFalse(us01_dates_before_current_date(self.family.divorce_date, "Divorce date", self.family))

    def test_us02_birth_before_marriage(self):
        self.assertFalse(us02_birth_before_marriage(self.individual.birth_date, self.family.marriage_date, self.individual.get_full_name(), self.individual.id, self.family.id))

        self.individual.set_birth_date("12 DEC 2068")
        self.assertTrue(us02_birth_before_marriage(self.individual.birth_date, self.family.marriage_date, self.individual.get_full_name(), self.individual.id, self.family.id))

    def test_us07_age_less_than_150(self):
        self.assertTrue(us07_age_less_than_150(self.individual.birth_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))
        
        self.individual.set_birth_date("15 Feb 2012")
        self.individual.set_death_date("21 Jan 2000")
        
        self.assertFalse(us07_age_less_than_150(self.individual.birth_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))
        
        self.individual.set_birth_date("05 Jan 1960")
        self.individual.set_death_date("21 Mar 2000")
        
        self.assertTrue(us07_age_less_than_150(self.individual.birth_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))
        
        self.individual.set_birth_date("25 SEP 1760")
        self.individual.set_death_date("11 Jan 2000")
        
        self.assertFalse(us07_age_less_than_150(self.individual.birth_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))
    
    def test_us08_birth_before_marriage_of_parents(self):
        self.individual.set_birth_date("15 Feb 2008")
        
        self.assertTrue(us08_birth_before_marriage_of_parents(self.individual.birth_date, self.family.marriage_date, self.family.divorce_date, self.individual.get_full_name(), self.individual.id, self.family.id))
        
        self.individual.set_birth_date("15 Feb 2008")
        self.family.set_marriage_date("11 Mar 2004")
        self.family.set_divorce_date("15 Jun 2010")
        
        self.assertTrue(us08_birth_before_marriage_of_parents(self.individual.birth_date, self.family.marriage_date, self.family.divorce_date, self.individual.get_full_name(), self.individual.id, self.family.id))
        
        self.individual.set_birth_date("25 Jan 2015")
        self.family.set_marriage_date("01 Sep 2004")
        self.family.set_divorce_date("15 Jun 2010")
        
        self.assertFalse(us08_birth_before_marriage_of_parents(self.individual.birth_date, self.family.marriage_date, self.family.divorce_date, self.individual.get_full_name(), self.individual.id, self.family.id))
    
if __name__ == "__main__":
    unittest.main(exit=False)