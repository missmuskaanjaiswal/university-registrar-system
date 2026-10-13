"""Manage student records."""

from .models import Student
from .exceptions import (
    InvalidStudentError,
    StudentNotFoundError,
)


class Registrar:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if not isinstance(student, Student):
            raise InvalidStudentError(
                "A valid Student object is required."
            )

        if student.student_id in self.students:
            raise InvalidStudentError(
                "Student ID already exists."
            )

        self.students[student.student_id] = student
        return student

    def get_student(self, student_id):
        student_id = str(student_id).strip()

        if student_id not in self.students:
            raise StudentNotFoundError(
                f"Student {student_id} was not found."
            )

        return self.students[student_id]

    def list_students(self):
        return list(self.students.values())

    def remove_student(self, student_id):
        student_id = str(student_id).strip()

        if student_id not in self.students:
            raise StudentNotFoundError(
                f"Student {student_id} was not found."
            )

        return self.students.pop(student_id)

    def load_students(self, students):
        for student in students:
            self.add_student(student)
