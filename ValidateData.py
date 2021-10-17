from datetime import datetime

import ReportUtils
from Family import Family
from Individual import Individual

individual_list = []
family_list = []


def get_family_by_family_id(family_id):
    for family in family_list:
        if family.get_id() == family_id:
            return family


def us01_dates_before_current_date(date, date_type, object_passed):
    if not date < datetime.now():
        if type(object_passed) is Individual:
            ReportUtils.add_error_found("Error US01: " + str(date_type) + " of " + object_passed.get_full_name() + " (" + str(object_passed.id) + ") occurs before current date.")

        if type(object_passed) is Family:
            ReportUtils.add_error_found("Error US01: " + str(date_type) + " of Family (" + str(object_passed.id) + ") occurs before current date.")

        return False
    else:
        return True


def us02_birth_before_marriage(birth_date, marriage_date, indiv_name, indiv_id, family_id):
    if birth_date > marriage_date:
        ReportUtils.add_error_found("Error US02: Birth date of " + str(indiv_name) + " (" + str(indiv_id) + ") occurs before marriage date. (" + str(family_id) + ")")
        return True
    else:
        return False


def is_indiv_valid(indiv):
    is_valid = True

    if indiv.name is None:
        is_valid = False
        indiv_name = str('Person with ID ' + indiv.id)
        ReportUtils.add_error_found("Error: " + indiv_name + " cannot have empty name.")
    else:
        indiv_name = indiv.get_full_name()

    if indiv.birth_date is None:
        is_valid = False
        ReportUtils.add_null_error_for_indiv(indiv_name, "Birth date")

    return is_valid


def is_fam_valid(fam):
    is_valid = True

    if fam.marriage_date is None:
        is_valid = False
        ReportUtils.add_null_error_for_fam(fam.id, "Marriage date")

    return is_valid


def validate_data(individuals, families):
    global individual_list
    individual_list = individuals

    global family_list
    family_list = families

    for indiv in individual_list:
        if is_indiv_valid(indiv):
            us01_dates_before_current_date(indiv.birth_date, 'Birth date', indiv)

            if indiv.death_date is not None:
                us01_dates_before_current_date(indiv.death_date, 'Death date', indiv)

            if indiv.get_family_id_as_spouse() != 'NA':
                for family_id in indiv.family_id_as_spouse:
                    family_data = get_family_by_family_id(family_id)

                    if family_data is not None and family_data.marriage_date is not None:
                        us02_birth_before_marriage(indiv.birth_date, family_data.marriage_date, indiv.get_full_name(), str(indiv.id), str(family_id))

    for family in family_list:
        if is_fam_valid(family):
            us01_dates_before_current_date(family.marriage_date, 'Marriage date', family)

            if family.divorce_date is not None:
                us01_dates_before_current_date(family.divorce_date, 'Divorce date', family)

    ReportUtils.compile_report()
