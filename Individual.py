from datetime import datetime


class Individual:
    DATE_FORMAT_INPUT = '%d %b %Y'
    DATE_FORMAT_OUTPUT = '%Y-%m-%d'

    def __init__(self, id):
        self.id = id
        self.name = None
        self.gender = None
        self.birth_date = None
        self.death_date = None
        self.alive = True
        self.family_id_as_child = None
        self.family_id_as_spouse = []

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_birth_date(self, birth_date):
        self.birth_date = datetime.strptime(birth_date, self.DATE_FORMAT_INPUT)

    def get_birth_date(self):
        if self.birth_date is not None:
            return self.birth_date.strftime(self.DATE_FORMAT_OUTPUT)

    def set_death_date(self, death_date):
        self.alive = False
        self.death_date = datetime.strptime(death_date, self.DATE_FORMAT_INPUT)

    def get_death_date(self):
        if self.death_date is not None:
            return self.death_date.strftime(self.DATE_FORMAT_OUTPUT)
        else:
            return 'NA'

    def get_alive(self):
        return self.alive

    def set_family_id_as_child(self, family_id_as_child):
        self.family_id_as_child = family_id_as_child

    def get_family_id_as_child(self):
        return self.family_id_as_child

    def set_family_id_as_spouse(self, family_id_as_spouse):
        self.family_id_as_spouse.append(family_id_as_spouse)

    def get_family_id_as_spouse(self):
        if not self.family_id_as_spouse:
            return 'NA'
        else:
            return '{\'' + '\', \''.join([str(famId) for famId in self.family_id_as_spouse]) + '\'}'

    def get_age(self):
        return relativedelta(datetime.now(), self.birth_date).years

    def get_full_name(self):
        return str(self.name).replace('/', '')
