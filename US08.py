import datetime
from datetime import datetime, timedelta, date
from typing import Optional, Dict, List


class Individual:
    """ assign a viduale record """
    def __init__(self, _id=None, name=None, sex=None, birt=None, alive=True, deat=False):
        """ assign Individual information """
        self.id = _id
        self.name = name
        self.sex = sex
        self.birt: Optional[Dict[str, str]] = birt
        self.alive = alive
        self.deat: Optional[bool, Dict[str, str]] = deat
        self.famc: List[str] = []
        self.fams: List[str] = []

    def age(self):
        """ calculate age using the birth date """
        today = date.today()
        birthday = datetime.strptime(self.birt['date'], "%d %b %Y")
        age = today.year - birthday.year - \
              ((today.month, today.day) < (birthday.month, birthday.day))
        return age

    def info(self):
        """ return Individual information with all data """
        alive = True if self.deat is False else False
        death = 'NA' if self.deat is False else self.deat['date']
        child = 'NA' if len(self.famc) == 0 else self.famc
        spouse = 'NA' if len(self.fams) == 0 else self.fams
        return [self.id, self.name, self.sex, self.birt['date'],
                self.age(), alive, death, child, spouse]


class Family:
    """ holds a Family record """
    def __init__(self, _id=None, marr=None, husb=None, wife=None, div=False):
        """ store Family info """
        self.id = _id
        self.marr = marr
        self.husb = husb
        self.wife = wife
        self.chil: List[str] = []
        self.div: Optional[bool, Dict[str, str]] = div

    def info(self, individuals: List[Individual]):
        """ return Family info """
        div = 'NA' if self.div is False else self.div['date']
        chil = 'NA' if len(self.chil) == 0 else self.chil
        h_name = next(individual.name for individual in individuals if individual.id == self.husb)
        w_name = next(individual.name for individual in individuals if individual.id == self.wife)

        return [self.id, self.marr['date'], div, self.husb, h_name, self.wife, w_name, chil]

  
def birth_before_marriage_of_parents(family: Family, individuals: List[Individual]) -> bool:
    """ user story: verify that divorce before death of either spouse and child birth is before marrige or not """
    mrgdate = datetime.strptime(family.marr.get('date'), "%d %b %Y")
    divdate = datetime.strptime(family.div.get('date'), "%d %b %Y")
    birthdate_child = datetime.strptime(individuals.birt.get('date'), "%d %b %Y")
 
    if family.marr:
        if birthdate_child - mrgdate > timedelta(minutes=0) and birthdate_child - divdate < timedelta(days=275):
            print(f"({family.id}) : birth_before_marriage_of_parents")
            return True
        else:
            print(f"({family.id}) : not birth_before_marriage_of_parents")
            return False
    else:
        print(f"({family.id}) : marrige is not happen")
        return False

