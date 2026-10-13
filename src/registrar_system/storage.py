"""Save and load student records in JSON and CSV formats."""

import csv
import json
from pathlib import Path

from .models import Student
from .exceptions import RegistrarError, InvalidStudentError


FIELDS = ["student_id", "name", "age", "course"]


def save_json(students, filename):
    path = Path(filename)
    try:
        data = [student.to_dict() for student in students]
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except (OSError, TypeError, ValueError) as exc:
        raise RegistrarError("Could not save JSON data.") from exc


def load_json(filename):
    path = Path(filename)
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise InvalidStudentError(
                "JSON data must contain a list of students."
            )

        return [Student.from_dict(item) for item in data]
    except (OSError, json.JSONDecodeError) as exc:
        raise RegistrarError("Could not load JSON data.") from exc


def save_csv(students, filename):
    path = Path(filename)
    try:
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())
    except (OSError, TypeError, ValueError) as exc:
        raise RegistrarError("Could not save CSV data.") from exc


def load_csv(filename):
    path = Path(filename)
    try:
        with path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != FIELDS:
                raise InvalidStudentError(
                    "CSV headers do not match the required fields."
                )

            students = []
            for row in reader:
                row["age"] = int(row["age"])
                students.append(Student.from_dict(row))
            return students
    except (OSError, csv.Error, ValueError) as exc:
        raise RegistrarError("Could not load CSV data.") from exc
