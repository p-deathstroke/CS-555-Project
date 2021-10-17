import datetime
from datetime import datetime, timedelta, date

import ReportUtils
from Family import Family
from Individual import Individual

individual_list = []
family_list = []


def get_family_by_family_id(family_id):
    for family in family_list:
        if family.get_id() == family_id:
            return family


def us07_age_less_than_150(birth_date, death_date, indiv_name, indiv_id, family_id) -> bool:
    current_date: datetime = datetime.now()
    years_150 = timedelta(days=54750)

    if death_date:
        if birth_date - death_date > timedelta(days=0): 
            ReportUtils.add_error_found("Error US07: Age of " + str(indiv_name) + " (" + str(indiv_id) + ") is Greater than 150 years. (" + str(family_id) + ")")
            return False
        elif death_date - birth_date < years_150: 
            return True
    else:
        if current_date - birth_date < years_150: return True
    ReportUtils.add_error_found("Error US07: Age of " + str(indiv_name) + " (" + str(indiv_id) + ") is not Greater than 150 years. (" + str(family_id) + ")")
            
    return False

def us08_birth_before_marriage_of_parents(birth_date, marriage_date, divorce_date, indiv_name, indiv_id, family_id) -> bool:
    
    if marriage_date:
        if birth_date - marriage_date > timedelta(minutes=0) and birth_date - divorce_date < timedelta(days=275):
            return True
        else:
            ReportUtils.add_error_found("Error US08:  "+ str(indiv_name) +  " (" + str(indiv_id) + ") has not birth before the marrige of Parents. (" + str(family_id) + ")")
            return False
    else:
        ReportUtils.add_error_found("Error US08:  "+ str(indiv_name) +  " (" + str(indiv_id) + ") Parents did not done Marrige. (" + str(family_id) + ")")
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
            if indiv.death_date is not None:
                us07_age_less_than_150(indiv.birth_date, indiv.death_date, indiv.get_full_name, str(indiv.id))
 
    for family in family_list:
        if is_fam_valid(family):
            if indiv.get_family_id_as_spouse() != 'NA':
                for family_id in indiv.family_id_as_spouse:
                    family_data = get_family_by_family_id(family_id)

                    if family_data is not None and family_data.marriage_date is not None:
                        us08_birth_before_marriage_of_parents(indiv.birth_date, family_data.marriage_date,  family_data.divorce_date, indiv.get_full_name(), str(indiv.id), str(family_id))

    ReportUtils.compile_report()
