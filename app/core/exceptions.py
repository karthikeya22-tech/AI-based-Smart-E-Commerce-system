class AppException(Exception):
    """Base exception for application-specific failures."""


class NotFoundError(AppException):
    """Raised when a requested resource does not exist."""


class AuthenticationError(AppException):
    """Raised when authentication is missing or invalid."""


class ValidationError(AppException):
    """Raised when request data fails business validation."""


class ServiceUnavailableError(AppException):
    """Raised when a downstream service cannot be reached."""
