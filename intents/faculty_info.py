def get_email(faculty_name):
    return f'SELECT email FROM faculty WHERE name = "{faculty_name}"'

def get_phone_number(faculty_name):
    return f'SELECT contact FROM faculty where name = "{faculty_name}"'

def get_office_loc(faculty_name):
    return f'SELECT office FROM faculty WHERE name = "{faculty_name}"'