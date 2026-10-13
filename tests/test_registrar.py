import pytest

from registrar_system.models import Student
from registrar_system.manager import Registrar
from registrar_system.exceptions import (
    InvalidStudentError,
    StudentNotFoundError,
)


def make_student():
    return Student("S101", "Aman", 20, "AIDS")


def test_student_creation():
    student = make_student()
    assert student.name == "Aman"
    assert student.age == 20


def test_student_to_dict():
    student = make_student()
    assert student.to_dict()["student_id"] == "S101"


def test_invalid_student_name():
    with pytest.raises(InvalidStudentError):
        Student("S102", "  ", 20, "AIDS")


def test_invalid_student_age():
    with pytest.raises(InvalidStudentError):
        Student("S103", "Riya", 0, "AIDS")


def test_add_and_get_student():
    registrar = Registrar()
    student = make_student()
    registrar.add_student(student)
    assert registrar.get_student("S101") == student


def test_duplicate_student():
    registrar = Registrar()
    registrar.add_student(make_student())
    with pytest.raises(InvalidStudentError):
        registrar.add_student(make_student())


def test_list_students():
    registrar = Registrar()
    registrar.add_student(make_student())
    assert len(registrar.list_students()) == 1


def test_remove_student():
    registrar = Registrar()
    registrar.add_student(make_student())
    registrar.remove_student("S101")
    assert registrar.list_students() == []


def test_missing_student():
    registrar = Registrar()
    with pytest.raises(StudentNotFoundError):
        registrar.get_student("S999")
