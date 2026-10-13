University Registrar System

A Python-based University Registrar System developed using Object-Oriented Programming (OOP). It manages student records and supports JSON and CSV file storage.

Features

- Add, view, and remove student records.
- Validate student information.
- Handle errors using custom exceptions.
- Save and load student records in JSON format.
- Save and load student records in CSV format.
- Automated unit tests using pytest.
- Continuous integration using GitHub Actions.
- Test coverage reporting.

Project Structure

university-registrar-system/
├── src/
│   └── registrar_system/
│       ├── __init__.py
│       ├── exceptions.py
│       ├── models.py
│       ├── manager.py
│       └── storage.py
├── tests/
│   ├── test_registrar.py
│   └── test_storage.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── pyproject.toml
└── README.md

Requirements

- Python 3.11 or compatible Python version
- pip
- pytest for running tests

Installation

Clone the repository:

git clone https://github.com/missmuskaanjaiswal/university-registrar-system.git
cd university-registrar-system

Install the project with testing dependencies:

pip install -e ".[test]"

Running Tests

Run the automated tests and check coverage:

pytest

The test suite checks student validation, registrar operations, custom exceptions, and JSON/CSV storage.

Continuous Integration

GitHub Actions automatically runs the test suite when changes are pushed to the repository. The workflow is defined in ".github/workflows/tests.yml".

Learning Objectives

- Understand Python classes and objects.
- Apply data validation and custom exceptions.
- Work with JSON and CSV files.
- Write automated unit tests.
- Use GitHub and GitHub Actions.

Author

Muskaan Jaiswal

License

This project was created for educational and internship purposes.
