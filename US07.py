import datetime
from datetime import datetime, timedelta, date
from typing import Optional, Dict, List


class Individual:
    """ holds an Individual record """
    def __init__(self, _id=None, name=None, sex=None, birt=None, alive=True, deat=False):
        """ store Individual info """
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
        """ return Individual info """
        alive = True if self.deat is False else False
        death = 'NA' if self.deat is False else self.deat['date']
        child = 'NA' if len(self.famc) == 0 else self.famc
        spouse = 'NA' if len(self.fams) == 0 else self.fams
        return [self.id, self.name, self.sex, self.birt['date'],
                self.age(), alive, death, child, spouse]



def less_than_150(individual: Individual) -> bool:
    birth_date: datetime = datetime.strptime(individual.birt['date'], "%d %b %Y")
    current_date: datetime = datetime.now()
    years_150 = timedelta(days=54750)

    if individual.deat:
        death_date: datetime = datetime.strptime(individual.deat['date'], "%d %b %Y")
        if birth_date - death_date > timedelta(days=0): return False
        elif death_date - birth_date < years_150: return True

    else:
        if current_date - birth_date < years_150: return True
    
    return False

