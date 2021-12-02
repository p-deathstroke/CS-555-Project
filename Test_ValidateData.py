import unittest

import ValidateData
from Family import Family
from Individual import Individual
from typing import List

from ValidateData import us01_dates_before_current_date, us02_birth_before_marriage, us03_birth_before_death, \
    us04_marriage_before_divorce, us07_age_less_than_150, us08_birth_before_marriage_of_parents, \
    us05_marriage_before_death, us06_divorce_before_death, us15_fewer_than_15_siblings, us16_male_last_names, \
    us09_birth_before_death_of_parents, us10_marriage_after_14, us11_no_bigamy, us12_parents_not_too_old, \
    us18_siblings_should_not_marry, us17_no_marriages_to_descendants, us23_unique_name_and_birth, us24_unique_family_by_spouses,us19_first_cousins_should_not_marry,us20_aunts_and_uncles,  us31_isSingleAliveOver30, us32_hasMultipleBirths, \
    us27_include_individual_ages,us28_order_siblings_by_age, us25_unique_first_names_in_families, us26_corresponding_entries


class TestValidateDataMethod(unittest.TestCase):
    def setUp(self):
        self.individual = Individual("Indiv1")
        self.individual.set_name("Individual /1/")
        self.individual.set_birth_date("12 DEC 1968")
        self.individual.set_death_date("18 JAN 2021")
        self.individual.set_family_id_as_spouse("Fam1")
        ValidateData.individual_list.append(self.individual)

        self.individual2 = Individual("Indiv2")
        self.individual.set_name("Individual /2/")
        self.individual2.set_birth_date("1 APR 1968")
        self.individual2.set_death_date("13 AUG 2021")
        self.individual2.set_family_id_as_spouse("Fam1")
        ValidateData.individual_list.append(self.individual2)

        self.individual3 = Individual("Indiv3")
        self.individual.set_name("Individual /3/")
        self.individual3.set_birth_date("13 AUG 2021")
        self.individual3.set_family_id_as_child("Fam1")
        ValidateData.individual_list.append(self.individual3)

        self.family = Family("Fam1")
        self.family.set_husb("Indiv1")
        self.family.set_wife("Indiv2")
        self.family.set_children("Indiv3")
        self.family.set_marriage_date("5 DEC 2001")
        self.family.set_divorce_date("10 JUL 2011")
        ValidateData.family_list.append(self.family)

        self.family2 = Family("Fam2")
        self.family2.set_husb("Indiv4")
        self.family2.set_wife("Indiv3")
        self.family2.set_children("Indiv")
        self.family2.set_marriage_date("5 DEC 2020")
        ValidateData.family_list.append(self.family2)

        self.family3 = Family("Fam3")
        self.family3.set_husb("Indiv3")
        self.family3.set_wife("Indiv7")
        self.family3.set_children("Indiv2")
        self.family3.set_marriage_date("5 DEC 2020")
        ValidateData.family_list.append(self.family3)

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
    
    def test_us05_marriage_before_death(self):
        self.assertTrue(us05_marriage_before_death(self.family.marriage_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

        self.family.set_marriage_date("05 Jan 1999")
        self.individual.set_death_date("21 Mar 1860")
        self.assertFalse(us05_marriage_before_death(self.family.marriage_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

        self.family.set_marriage_date("05 Jan 1992")
        self.individual.set_death_date("21 Mar 2060")
        self.assertTrue(us05_marriage_before_death(self.family.marriage_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

        self.family.set_marriage_date("05 Jan 2020")
        self.individual.set_death_date("21 Mar 1960")
        self.assertFalse(us05_marriage_before_death(self.family.marriage_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

    def test_us06_divorce_before_death(self):
        self.assertTrue(us06_divorce_before_death(self.family.divorce_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

        self.family.set_divorce_date("11 Jan 2021")
        self.individual.set_death_date("15 Jun 2007")
        self.assertFalse(us06_divorce_before_death(self.family.divorce_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

        self.family.set_divorce_date("11 Mar 2000")
        self.individual.set_death_date("15 Jun 2019")
        self.assertTrue(us06_divorce_before_death(self.family.divorce_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

        self.family.set_divorce_date("11 Mar 2012")
        self.individual.set_death_date("15 Jun 2001")
        self.assertFalse(us06_divorce_before_death(self.family.divorce_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id, self.family.id))

    def test_us03_birth_before_death(self):
        self.assertTrue(us03_birth_before_death(self.individual.birth_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id))

        self.individual.set_birth_date("05 Jan 2000")
        self.individual.set_death_date("21 Mar 1760")
        self.assertFalse(us03_birth_before_death(self.individual.birth_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id))

        self.individual.set_birth_date("05 Jan 1997")
        self.individual.set_death_date("21 Mar 2050")
        self.assertTrue(us03_birth_before_death(self.individual.birth_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id))

        self.individual.set_birth_date("05 Jan 2056")
        self.individual.set_death_date("21 Mar 1960")
        self.assertFalse(us03_birth_before_death(self.individual.birth_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id))

    def test_us04_marriage_before_divorce(self):
        self.assertTrue(us04_marriage_before_divorce(self.family.marriage_date, self.family.divorce_date, self.individual.get_full_name(), self.individual.id, self.family.id))

        self.individual.set_birth_date("14 Jun 1997")
        self.family.set_marriage_date("11 Mar 2021")
        self.family.set_divorce_date("15 Jun 2010")
        self.assertFalse(us04_marriage_before_divorce(self.family.marriage_date, self.family.divorce_date, self.individual.get_full_name(), self.individual.id, self.family.id))

        self.individual.set_birth_date("17 Oct 1960")
        self.family.set_marriage_date("11 Mar 2004")
        self.family.set_divorce_date("15 Jun 2010")
        self.assertTrue(us04_marriage_before_divorce(self.family.marriage_date, self.family.divorce_date, self.individual.get_full_name(), self.individual.id, self.family.id))

        self.individual.set_birth_date("11 Jun 1964")
        self.family.set_marriage_date("11 Mar 2016")
        self.family.set_divorce_date("15 Jun 2010")
        self.assertFalse(us04_marriage_before_divorce(self.family.marriage_date, self.family.divorce_date, self.individual.get_full_name(), self.individual.id, self.family.id))

    def test_us07_age_less_than_150(self):
        self.assertTrue(us07_age_less_than_150(self.individual.birth_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id))
        
        self.individual.set_birth_date("15 Feb 2012")
        self.individual.set_death_date("21 Jan 2000")
        
        self.assertFalse(us07_age_less_than_150(self.individual.birth_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id))
        
        self.individual.set_birth_date("05 Jan 1960")
        self.individual.set_death_date("21 Mar 2000")
        
        self.assertTrue(us07_age_less_than_150(self.individual.birth_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id))
        
        self.individual.set_birth_date("25 SEP 1760")
        self.individual.set_death_date("11 Jan 2000")
        
        self.assertFalse(us07_age_less_than_150(self.individual.birth_date, self.individual.death_date, self.individual.get_full_name(), self.individual.id))
    
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

    def test_us09_birth_before_death_of_parents(self):
        # parents death occur after birth
        self.assertFalse(us09_birth_before_death_of_parents(self.individual3.birth_date, self.individual2.death_date, self.individual.death_date, self.individual3.get_full_name(), self.individual3.get_id(), self.family.id))

        # both parents death occur before birth
        self.individual.set_death_date("11 JAN 2020")
        self.individual2.set_death_date("10 AUG 2021")
        self.assertTrue(us09_birth_before_death_of_parents(self.individual3.birth_date, self.individual2.death_date, self.individual.death_date, self.individual3.get_full_name(), self.individual3.get_id(), self.family.id))

        # mother death occur before birth
        self.individual.set_death_date("18 JAN 2021")
        self.assertTrue(us09_birth_before_death_of_parents(self.individual3.birth_date, self.individual2.death_date, self.individual.death_date, self.individual3.get_full_name(), self.individual3.get_id(), self.family.id))

        # father death occur before birth
        self.individual.set_death_date("11 JAN 2020")
        self.individual2.set_death_date("13 AUG 2021")
        self.assertTrue(us09_birth_before_death_of_parents(self.individual3.birth_date, self.individual2.death_date, self.individual.death_date, self.individual3.get_full_name(), self.individual3.get_id(), self.family.id))

        self.assertFalse(us09_birth_before_death_of_parents(None, None, None, None, None, None))

    def test_us10_marriage_after_14(self):
        # both spouses were over 14 when marriage happened
        self.assertFalse(us10_marriage_after_14(self.family.marriage_date, self.individual2.birth_date, self.individual.birth_date, self.family.id))

        # both spouses were under 14 when marriage happened
        self.individual2.set_birth_date("1 APR 2020")
        self.individual.set_birth_date("12 DEC 2019")
        self.assertTrue(us10_marriage_after_14(self.family.marriage_date, self.individual2.birth_date, self.individual.birth_date, self.family.id))

        # wife was under 14 when marriage happened
        self.individual.set_birth_date("12 DEC 1968")
        self.assertTrue(us10_marriage_after_14(self.family.marriage_date, self.individual2.birth_date, self.individual.birth_date, self.family.id))

        # husband was under 14 when marriage happened
        self.individual.set_birth_date("12 DEC 2020")
        self.individual2.set_birth_date("1 APR 1968")
        self.assertTrue(us10_marriage_after_14(self.family.marriage_date, self.individual2.birth_date, self.individual.birth_date, self.family.id))

        self.assertFalse(us10_marriage_after_14(None, None, None, self.family.id))
        self.assertFalse(us10_marriage_after_14(self.family.marriage_date, None, None, self.family.id))

    def test_us15_fewer_than_15_siblings(self):
        self.family.set_husb("I0")
        self.family.set_wife("I1")
        self.family.set_children("I2")
        self.family.set_children("I3")
        self.family.set_children("I4")
        self.family.set_children("I5")
        self.family.set_children("I6")
        self.family.set_children("I7")
        self.family.set_children("I8")
        self.family.set_children("I9")
        self.family.set_children("I10")
        self.family.set_children("I11")
        self.family.set_children("I12")
        self.family.set_children("I13")
        self.family.set_children("I14")
        self.family.set_children("I15")
        self.family.set_children("I16")
        self.family.set_children("I17")
        self.assertFalse(us15_fewer_than_15_siblings(self.family))
        
        self.family.children = []
        self.family.set_children("I2")
        self.family.set_children("I3")
        self.family.set_children("I4")
        self.family.set_children("I5")
        self.family.set_children("I6")
        self.family.set_children("I7")
        self.family.set_children("I8")
        self.assertTrue(us15_fewer_than_15_siblings(self.family))
        
    def test_us16_male_last_names(self):
        individuals = []
        self.individual = Individual("Indv0")
        self.individual.set_name("Pablo /Escobar/")
        self.individual.set_gender('M')
        self.family.set_husb("Indv0")
        individuals.append(self.individual)
        self.individual = Individual("Indv1")
        self.individual.set_name("Veronika /Esco/")
        self.individual.set_gender('F')
        self.family.set_wife("Indv1")
        individuals.append(self.individual)
        self.individual = Individual("Indv2")
        self.individual.set_name("Terry /Escobart/")
        self.individual.set_gender('M')
        self.family.set_children("Indv2")
        individuals.append(self.individual)
        self.individual = Individual("Indv3")
        self.individual.set_name("Maria /Escobar/")
        self.individual.set_gender('F')
        self.family.set_children("Indv3")
        individuals.append(self.individual)
        self.assertFalse(us16_male_last_names(self.family.husb, self.family.wife, self.family.children, individuals))
        
        individuals = []
        self.individual = Individual("Indv0")
        self.individual.set_name("Danis /Hazard/")
        self.individual.set_gender('M')
        self.family.set_husb("Indv0")
        individuals.append(self.individual)
        self.individual = Individual("Indv1")
        self.individual.set_name("Vina /Hazard/")
        self.individual.set_gender('F')
        self.family.set_wife("Indv1")
        individuals.append(self.individual)
        self.individual = Individual("Indv2")
        self.individual.set_name("JR /Hazard/")
        self.individual.set_gender('M')
        self.family.set_children("Indv2")
        individuals.append(self.individual)
        self.individual = Individual("Indv3")
        self.individual.set_name("SR /Hazard/")
        self.individual.set_gender('M')
        self.family.set_children("Indv3")
        individuals.append(self.individual)
        self.assertTrue(us16_male_last_names(self.family.husb, self.family.wife, self.family.children, individuals))

        individuals = []
        self.individual = Individual("Indv0")
        self.individual.set_name("Nick /Walter/")
        self.individual.set_gender('M')
        self.family.set_husb("Indv0")
        individuals.append(self.individual)
        self.individual = Individual("Indv1")
        self.individual.set_name("Moni /Walter/")
        self.individual.set_gender('F')
        self.family.set_wife("Indv1")
        individuals.append(self.individual)
        self.individual = Individual("Indv2")
        self.individual.set_name("Maris /Walter/")
        self.individual.set_gender('M')
        self.family.set_children("Indv2")
        individuals.append(self.individual)
        self.individual = Individual("Indv3")
        self.individual.set_name("Haly /Walters/")
        self.individual.set_gender('M')
        self.family.set_children("Indv3")
        individuals.append(self.individual)
        self.assertFalse(us16_male_last_names(self.family.husb, self.family.wife, self.family.children, individuals))


    def test_us23_unique_name_and_birth(self):
        indi1: Individual = Individual(_id="I1", name="John Doe", birt={'date': "14 OCT 1990"})
        indi2: Individual = Individual(_id="I2", name="John Doe", birt={'date': "14 OCT 1990"})
        indi3: Individual = Individual(_id="I3", name="Nidhi Patel", birt={'date': "1 OCT 1998"})
        indi4: Individual = Individual(_id="I4", name="Patrik Kim", birt={'date': "4 NOV 2000"})
        indi5: Individual = Individual(_id="I5", name="John Hill", birt={'date': "11 JAN 2010"})
        individuals: List[Individual] = [indi1, indi2, indi3, indi4, indi5]
        self.assertEqual(us23_unique_name_and_birth(individuals), [["I2", "John Doe", "14 OCT 1990"]])

    def test_us24_unique_family_by_spouses(self):
        fam1: Family = Family(_id="I1", husb="John Doe1", wife="jennifer Doe1",
                              marr={'date': "14 OCT 1993"})
        fam2: Family = Family(_id="I2", husb="John Doe1", wife="jennifer Doe1",
                              marr={'date': "14 OCT 1993"})
        fam3: Family = Family(_id="I3", husb="Anurag Kim", wife="Emma Green",
                              marr={'date': "1 OCT 1998"})
        fam4: Family = Family(_id="I4", husb="Shrey Hill", wife="Olivia Kim",
                              marr={'date': "4 NOV 2000"})
        fam5: Family = Family(_id="I5", husb="Parthik Smith", wife="Sophia Taylor",
                              marr={'date': "11 JAN 2010"})
        families: List[Family] = [fam1, fam2, fam3, fam4, fam5]
        self.assertEqual(us24_unique_family_by_spouses(families),
                         [["I2", "John Doe1", "jennifer Doe1", "14 OCT 1993"]])

    def test_us11_no_bigamy(self):
        self.assertTrue(us11_no_bigamy(self.family))
        self.assertFalse(us11_no_bigamy(self.family))

    def test_us12_parents_not_too_old(self):
        husb_age = self.individual.set_age("18 Sep 1960")
        wife_age = self.individual.set_age("18 Dec 1964")
        child_age = self.individual.set_age("20 Apr 2000")
        self.assertTrue(us12_parents_not_too_old(husb_age, wife_age, child_age, self.individual.get_full_name(), self.individual.id, self.family.id))

        husb_age = self.individual.set_age("23 Jun 1920")
        wife_age = self.individual.set_age("14 Apr 1924")
        child_age= self.individual.set_age("11 Jul 2010")
        self.assertFalse(us12_parents_not_too_old(husb_age,wife_age,child_age, self.individual.get_full_name(),self.individual.id, self.family.id))

    def test_us19_first_cousins_should_not_marry(self):

        self.assertTrue(us19_first_cousins_should_not_marry(self.family))
        self.assertFalse(us19_first_cousins_should_not_marry(self.individual,self.family))

    def test_us20_aunts_and_uncles(self):
        self.assertTrue(us20_aunts_and_uncles())
        self.assertFalse(us20_aunts_and_uncles())


    def test_us17_no_marriages_to_descendants(self):
        self.assertFalse(us17_no_marriages_to_descendants(self.family.id, self.family.husb, self.family.wife, self.family2, self.family3))

        self.family4 = Family("Fam4")
        self.family4.set_husb("Indiv1")
        self.family4.set_wife("Indiv3")
        self.family4.set_marriage_date("5 DEC 2020")
        self.assertTrue(us17_no_marriages_to_descendants(self.family4.id, self.family4.husb, self.family4.wife, self.family2, self.family3))

        self.family4.set_husb("Indiv3")
        self.family4.set_wife("Indiv2")
        self.family4.set_marriage_date("5 DEC 2020")
        self.assertTrue(us17_no_marriages_to_descendants(self.family4.id, self.family4.husb, self.family4.wife, self.family2, self.family3))

        self.assertFalse(us17_no_marriages_to_descendants(self.family4.id, self.family4.husb, self.family4.wife, None, None))

    def test_us18_siblings_cannot_be_siblings(self):
        self.assertFalse(us18_siblings_should_not_marry(self.individual.family_id_as_child, self.individual2.family_id_as_child, self.family.id))

        self.individual.set_family_id_as_child("USF18F1")
        self.individual2.set_family_id_as_child("USF18F2")
        self.assertFalse(us18_siblings_should_not_marry(self.individual.family_id_as_child, self.individual2.family_id_as_child, self.family.id))

        self.individual.set_family_id_as_child("USF18F1")
        self.individual2.set_family_id_as_child("USF18F1")
        self.assertTrue(us18_siblings_should_not_marry(self.individual.family_id_as_child, self.individual2.family_id_as_child, self.family.id))

    def test_us25_unique_first_names_in_families(self):
        self.assertTrue(us25_unique_first_names_in_families(self.family.id, self.family.children))

        self.family.set_children("Indiv3")
        self.assertFalse(us25_unique_first_names_in_families(self.family.id, self.family.children))

        self.assertTrue(us25_unique_first_names_in_families(None, None))

    def test_us26_corresponding_entries(self):
        self.assertTrue(us26_corresponding_entries('Indiv3', 'INDIV'))
        self.assertTrue(us26_corresponding_entries('Fam1', 'FAMILY'))

        self.assertFalse(us26_corresponding_entries('Person1', 'INDIV'))
        self.assertFalse(us26_corresponding_entries('Family4', 'FAMILY'))

        self.assertFalse(us26_corresponding_entries(None, 'FAMILY'))
        self.assertFalse(us26_corresponding_entries('Indiv3', None))
        self.assertFalse(us26_corresponding_entries(None, None))

    def test_us31_isSingleAliveOver30(self):
        ind = us31_isSingleAliveOver30()
        # ind.age = 31
        ind.alive = True
        self.assertTrue(ind)

        ind = us31_isSingleAliveOver30()
        self.assertFalse(ind)

    def test_us32_hasMultipleBirths(self):
        birthdate1 = datetime.now()
        birthdate2 = datetime(2009, 10, 5, 18, 00)
        self.assertFalse(us32_hasMultipleBirths([birthdate1, birthdate2]))

        birthdate1 = datetime.datetime.now()
        birthdate2 = datetime.datetime.now()
        birthdate3 = datetime.datetime(2009, 10, 5, 18, 00)
        self.assertTrue(us32_hasMultipleBirths([birthdate1, birthdate2, birthdate3]))

    def test_us27_include_individual_ages(self):
        us27_include_individual_ages(self.birth_date,self.death_date)
    def test_us28_order_siblings_by_age(self):
        us27_include_individual_ages(self)

if __name__ == "__main__":
    unittest.main(exit=False)
