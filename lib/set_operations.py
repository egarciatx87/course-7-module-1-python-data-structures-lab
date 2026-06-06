# This module contains operations related to sets.

# def unique_majors(student_list):
#     """
#     Return a set of unique student majors using set comprehension.
#     Extract the major field from each student record.
#     """
def unique_majors(student_list):
    # A set comprehension looks through student[2] (the major) for every student
    return {student[2] for student in student_list}
