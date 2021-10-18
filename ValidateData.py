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

def us03_birth_before_death(birth_date, death_date, indiv_name, indiv_id, family_id):
    if birth_date > death_date:
        ReportUtils.add_error_found("Error US03: Death date of " + str(indiv_name) + " (" + str(indiv_id) + ") occurs before birth date. (" + str(family_id) + ")")
        return False
    else:
        return True

def us04_marriage_before_divorce(marriage_date, divorce_date, indiv_name, indiv_id, family_id):
    if marriage_date > divorce_date:
        ReportUtils.add_error_found("Error US04: Divorce date of " + str(indiv_name) + " (" + str(indiv_id) + ") occurs before marriage date. (" + str(family_id) + ")")
        return False
    else:
       return True
      
def us05_marriage_before_death(marriage_date, death_date, indiv_name, indiv_id, family_id):
     if marriage_date > death_date:
         ReportUtils.add_error_found("Error US05: Marriage date of " + str(indiv_name) + " (" + str(indiv_id) + ") occurs before death date. (" + str(family_id) + ")")
         return False
     else:
         return True

def us06_divorce_before_death(divorce_date, death_date, indiv_name, indiv_id, family_id):
     if divorce_date > death_date:
         ReportUtils.add_error_found("Error US06: Divorce date of " + str(indiv_name) + " (" + str(indiv_id) + ") occurs before death date. (" + str(family_id) + ")")
         return False
     else:
         return True    

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
            us03_birth_before_death(indiv.birth_date,indiv.death_date, indiv.get_full_name(), str(indiv.id), str(family_id))

            if indiv.death_date is not None:
                us01_dates_before_current_date(indiv.death_date, 'Death date', indiv)
                us05_marriage_before_death(indiv.marriage_date, family_data.death_date,indiv.get_full_name(), str(indiv.id),str(family_id))
                us03_birth_before_death(indiv.birth_date,indiv.death_date, indiv.get_full_name(), str(indiv.id), str(family_id))
                us07_age_less_than_150(indiv.birth_date, indiv.death_date, indiv.get_full_name, str(indiv.id))

            if indiv.get_family_id_as_spouse() != 'NA':
                for family_id in indiv.family_id_as_spouse:
                    family_data = get_family_by_family_id(family_id)

                    if family_data is not None and family_data.marriage_date is not None:
                        us02_birth_before_marriage(indiv.birth_date, family_data.marriage_date, indiv.get_full_name(), str(indiv.id), str(family_id))
                        us04_marriage_before_divorce(indiv.marriage_date, family_data.divorce_date,indiv.get_full_name(), str(indiv.id),str(family_id))

    for family in family_list:
        if is_fam_valid(family):
            us01_dates_before_current_date(family.marriage_date, 'Marriage date', family)

            if family.divorce_date is not None:
                us01_dates_before_current_date(family.divorce_date, 'Divorce date', family)
                us06_divorce_before_death(indiv.divorce_date, family_data.death_date,indiv.get_full_name(), str(indiv.id),str(family_id))
            
            if indiv.get_family_id_as_spouse() != 'NA':
                for family_id in indiv.family_id_as_spouse:
                    family_data = get_family_by_family_id(family_id)

                    if family_data is not None and family_data.marriage_date is not None:
                        us08_birth_before_marriage_of_parents(indiv.birth_date, family_data.marriage_date,  family_data.divorce_date, indiv.get_full_name(), str(indiv.id), str(family_id))

            if indiv.get_family_id_as_spouse() != 'NA':
                for family_id in indiv.family_id_as_spouse:
                    family_data = get_family_by_family_id(family_id)

                    if family_data is not None and family_data.marriage_date is not None:
                        us04_marriage_before_divorce(indiv.marriage_date, family_data.divorce_date,indiv.get_full_name(), str(indiv.id),str(family_id))

    ReportUtils.compile_report()