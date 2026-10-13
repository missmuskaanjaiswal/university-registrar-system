import pytest

from registrar_system.models import Student
from registrar_system.storage import (
    save_json,
    load_json,
    save_csv,
    load_csv,
)
from registrar_system.exceptions import RegistrarError


def sample_students():
    return [
        Student("S101", "Aman", 20, "AIDS"),
        Student("S102", "Riya", 21, "CSE"),
    ]


def test_json_save_and_load(tmp_path):
    file_path = tmp_path / "students.json"
    students = sample_students()

    save_json(students, file_path)
    loaded = load_json(file_path)

    assert loaded == students


def test_csv_save_and_load(tmp_path):
    file_path = tmp_path / "students.csv"
    students = sample_students()

    save_csv(students, file_path)
    loaded = load_csv(file_path)

    assert loaded == students


def test_invalid_json_file(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{invalid json", encoding="utf-8")

    with pytest.raises(RegistrarError):
        load_json(file_path)


def test_missing_json_file(tmp_path):
    file_path = tmp_path / "missing.json"

    with pytest.raises(RegistrarError):
        load_json(file_path)


def test_missing_csv_file(tmp_path):
    file_path = tmp_path / "missing.csv"

    with pytest.raises(RegistrarError):
        load_csv(file_path)
