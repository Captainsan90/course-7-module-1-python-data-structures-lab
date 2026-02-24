def student_generator(students, major):
    """
    Returns a generator expression for all students by major.
    """
    return (student for student in students if student[2] == major)