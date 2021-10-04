from datetime import datetime


class Family:
    DATE_FORMAT_INPUT = '%d %b %Y'
    DATE_FORMAT_OUTPUT = '%Y-%m-%d'

    def __init__(self, id):
        self.id = id
        self.husb = None
        self.wife = None
        self.marriage_date = None
        self.divorce_date = None
        self.children = []

    def get_id(self):
        return self.id

    def set_husb(self, husb):
        self.husb = husb

    def get_husb(self):
        return self.husb

    def set_wife(self, wife):
        self.wife = wife

    def get_wife(self):
        return self.wife

    def set_children(self, childId):
        self.children.append(childId)

    def get_children(self):
        if not self.children:
            return 'NA'
        else:
            return '{\'' + '\', \''.join([str(childId) for childId in self.children]) + '\'}'

    def set_marriage_date(self, marriage_date):
        self.marriage_date = datetime.strptime(marriage_date, self.DATE_FORMAT_INPUT)

    def get_marriage_date(self):
        if self.marriage_date is not None:
            return self.marriage_date.strftime(self.DATE_FORMAT_OUTPUT)

    def set_divorce_date(self, divorce_date):
        self.divorce_date = datetime.strptime(divorce_date, self.DATE_FORMAT_INPUT)

    def get_divorce_date(self):
        if self.divorce_date is not None:
            return self.divorce_date.strftime(self.DATE_FORMAT_OUTPUT)
        else:
            return 'NA'
