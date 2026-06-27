from .constants import (
    VALID_STACKS,
    VALID_LEVELS,
    BACKEND_PACKAGES,
    FRONTEND_PACKAGES,
)


def validate_log(stack, level, package, message):
    """
    Validate log request before sending it to the logging server.
    """

    if stack not in VALID_STACKS:
        raise ValueError(
            f"Invalid stack '{stack}'. Allowed: {VALID_STACKS}"
        )

    if level not in VALID_LEVELS:
        raise ValueError(
            f"Invalid level '{level}'. Allowed: {VALID_LEVELS}"
        )

    if stack == "backend":
        allowed_packages = BACKEND_PACKAGES
    else:
        allowed_packages = FRONTEND_PACKAGES

    if package not in allowed_packages:
        raise ValueError(
            f"Invalid package '{package}' for {stack} stack."
        )

    if not isinstance(message, str):
        raise ValueError("Message must be a string.")

    if not message.strip():
        raise ValueError("Message cannot be empty.")

    return True