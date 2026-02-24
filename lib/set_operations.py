def unique_majors(students):
    """
    Returns a set of unique student majors.
    """
    return {student[2] for student in students}