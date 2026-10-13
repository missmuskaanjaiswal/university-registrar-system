"""Student data model and validation."""

from dataclasses import dataclass
from .exceptions import InvalidStudentError


@dataclass
class Student:
    student_id: str
    name: str
    age: int
    course: str

    def __post_init__(self):
        self.student_id = str(self.student_id).strip()
        self.name = self.name.strip()
        self.course = self.course.strip()

        if not self.student_id:
            raise InvalidStudentError("Student ID is required.")

        if not self.name:
            raise InvalidStudentError("Student name is required.")

        if isinstance(self.age, bool) or not isinstance(self.age, int):
            raise InvalidStudentError("Age must be an integer.")

        if self.age <= 0:
            raise InvalidStudentError("Age must be positive.")

        if not self.course:
            raise InvalidStudentError("Course is required.")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
        }

    @classmethod
    def from_dict(cls, data):
        try:
            return cls(
                student_id=data["student_id"],
                name=data["name"],
                age=data["age"],
                course=data["course"],
            )
        except (KeyError, TypeError) as exc:
            raise InvalidStudentError(
                "Student record is incomplete or invalid."
            ) from exc
