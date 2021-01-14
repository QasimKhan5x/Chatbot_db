def get_credit_hours(course_name=None, course_code=None):
    if course_name:
        return f'SELECT creditHours FROM course WHERE courseName = "{course_name};"'
    else:
        return f'SELECT creditHours FROM course WHERE courseCode = "{course_code};"'

def get_course_code(course_name):
    return f'SELECT courseCode FROM course WHERE courseName = "{course_name};"'

def get_course_loc(course_name=None, course_code=None):
    pass

def get_course_teacher(course_name=None, course_code=None):
    if course_name:
        return f'SELECT instructor FROM course WHERE courseName = "{course_name};"'
    else:
        return f'SELECT instructor FROM course WHERE courseCode = "{course_code};"'

def get_course_time(course_name=None, course_code=None):
    pass
