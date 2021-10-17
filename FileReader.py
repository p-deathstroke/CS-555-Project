from Family import Family
from Individual import Individual
from prettytable import PrettyTable

from ValidateData import validate_data

output = open('project_04_output.txt', 'w')
individual_list_from_file = []
family_list_from_file = []
individual = None
family = None
prev_tag = None


def get_name_by_id(id):
    for indiv in individual_list_from_file:
        if indiv.get_id() == id:
            return indiv.get_name()


def print_tables(individual_list, family_list):
    individual_table = PrettyTable()
    individual_table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]

    family_table = PrettyTable()
    family_table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name",
                                "Children"]

    for indiv in individual_list:
        individual_table.add_row(
            [indiv.get_id(), indiv.get_name(), indiv.get_gender(), indiv.get_birth_date(), indiv.get_age(),
             indiv.get_alive(), indiv.get_death_date(), indiv.get_family_id_as_child(),
             indiv.get_family_id_as_spouse()])

    for fam in family_list:
        family_table.add_row([fam.get_id(), fam.get_marriage_date(), fam.get_divorce_date(), fam.get_husb(), get_name_by_id(fam.get_husb()), fam.get_wife(), get_name_by_id(fam.get_wife()), fam.get_children()])

    print('Individuals')
    print(individual_table)

    print('Families')
    print(family_table)

    output.write("Individuals\n")
    output.write(str(individual_table))
    output.write("\nFamilies\n")
    output.write(str(family_table))


def read_file(file_path):
    ged_file = open(str(file_path), 'r')
    for line in ged_file:
        line_words = line.split()

        if line_words[0] == '0':
            if line_words[1] in ['NOTE', 'TRLR', 'HEAD']:
                continue
            else:
                if line_words[2] in ['INDI', 'FAM']:
                    if line_words[2] == 'INDI':
                        individual = Individual(line_words[1])
                        individual_list_from_file.append(individual)
                    else:
                        family = Family(line_words[1])
                        family_list_from_file.append(family)

                    continue
                else:
                    continue
        if line_words[0] == '1':
            if line_words[1] in ['FAMC', 'NAME', 'SEX', 'BIRT', 'CHIL', 'MARR', 'WIFE', 'DEAT', 'DIV', 'FAMS', 'HUSB']:
                st = ' '.join(line_words[2:])

                if individual is not None:
                    if line_words[1] == 'FAMC':
                        individual.set_family_id_as_child(st)
                    elif line_words[1] == 'NAME':
                        individual.set_name(st)
                    elif line_words[1] == 'SEX':
                        individual.set_gender(st)
                    elif line_words[1] == 'CHIL':
                        family.set_children(st)
                    elif line_words[1] == 'WIFE':
                        family.set_wife(st)
                    elif line_words[1] == 'FAMS':
                        individual.set_family_id_as_spouse(st)
                    elif line_words[1] == 'HUSB':
                        family.set_husb(st)
                    else:
                        prev_tag = line_words[1]

                continue
            else:
                continue
        if line_words[0] == '2':
            if line_words[1] in ['DATE']:
                st = ' '.join(line_words[2:])

                if prev_tag is not None:
                    if prev_tag == 'BIRT':
                        individual.set_birth_date(st)
                    elif prev_tag == 'DEAT':
                        individual.set_death_date(st)
                    elif prev_tag == 'MARR':
                        family.set_marriage_date(st)
                    elif prev_tag == 'DIV':
                        family.set_divorce_date(st)

                continue
            else:
                continue

    print_tables(individual_list_from_file, family_list_from_file)
    validate_data(individual_list_from_file, family_list_from_file)

