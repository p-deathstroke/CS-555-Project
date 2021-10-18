import unittest

from Family import Family
from Individual import Individual
from ValidateData import us01_dates_before_current_date, us02_birth_before_marriage
from ValidateData import us05_marriage_before_death, us06_divorce_before_death


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
    
    def  test_us05_marriage_before_death(self):
         self.assertTrue(us05_marriage_before_death(self.individual.marriage_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

         self.individual.set_marriage_date("05 Jan 1999")
         self.individual.set_death_date("21 Mar 1860")
         self.assertFalse(us05_marriage_before_death(self.individual.marriage_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

         self.individual.set_marriage_date("05 Jan 1992")
         self.individual.set_death_date("21 Mar 2060")
         self.assertTrue(us05_marriage_before_death(self.individual.marriage_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

         self.individual.set_marriage_date("05 Jan 2020")
         self.individual.set_death_date("21 Mar 1960")
         self.assertFalse(us05_marriage_before_death(self.individual.marriage_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

    def  test_us06_divorce_before_death(self):
         self.assertTrue(us06_divorce_before_death(self.individual.divorce_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

         self.individual.set_divorce_date("11 Jan 2021")
         self.individual.set_death_date("15 Jun 2007")
         self.assertFalse(us06_divorce_before_death(self.individual.divorce_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

         self.individual.set_divorce_date("11 Mar 2000")
         self.individual.set_death_date("15 Jun 2019")
         self.assertTrue(us06_divorce_before_death(self.individual.divorce_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

         self.individual.set_divorce_date("11 Mar 2012")
         self.individual.set_death_date("15 Jun 2001")
         self.assertFalse(us06_divorce_before_death(self.individual.divorce_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))


if __name__ == "__main__":
    unittest.main(exit=False)
