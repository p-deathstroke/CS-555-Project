error_and_anomalies_list = []


def compile_report():
    if len(error_and_anomalies_list):
        report = open('error_report.ged', 'w')
        for message in error_and_anomalies_list:
            report.write(message + '\n')


def add_error_found(error_message):
    error_and_anomalies_list.append(error_message)


def add_null_error_for_indiv(indiv_name, field_found_none):
    error_and_anomalies_list.append("Error: " + str(field_found_none) + " of " + str(indiv_name) + " cannot be empty.")


def add_null_error_for_fam(family_id, field_found_none):
    error_and_anomalies_list.append("Error: " + str(field_found_none) + " of Family (" + str(family_id) + ") cannot be empty.")
