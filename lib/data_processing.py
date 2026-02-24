# data_processing.py

def format_student_data(student):
    """
    Returns a formatted string for a given student tuple.
    """
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(students):
    """
    Loops through all students and prints each student's details 
    """
    for student in students:
        print(format_student_data(student))