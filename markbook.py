"""
Markbook Application
Group members: Marcus Tuen Muk, Liu Chen Wu, Stella Hong
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    return {}

def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    classroom = {
        "course_code": course_code,
        "course_name": course_name,
        "Period": period,
        "Teacher": teacher 
    }
    with open("classroom.json", 'w') as f:
        json.dump(classroom)
    return classroom


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    return 0

def add_student_to_classroom(student, classroom):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """

    classroom["students"] = student

    return classroom
    pass
