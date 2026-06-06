# This module contains functions for filtering student data.

# def filter_students_by_major(student_list, major):
#     """
#     Return a filtered list of students by major using a list comprehension.
#     The function should:
#     - Check if a student's major matches the given major (case insensitive).
#     - Return a new list containing only students that match.
#     """
def filter_students_by_major(student_list, target_major):
    # Loops through the list, unpacks the tuple into id, name, major
    # Keeps the student tuple only if the major matches target_major
    return [student for student in student_list if student[2] == target_major]
