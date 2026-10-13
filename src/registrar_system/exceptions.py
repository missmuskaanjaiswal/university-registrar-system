"""Custom exceptions for the registrar system."""


class RegistrarError(Exception):
    """Base exception for registrar errors."""


class InvalidStudentError(RegistrarError):
    """Raised when student data is invalid."""


class StudentNotFoundError(RegistrarError):
    """Raised when a student does not exist."""
