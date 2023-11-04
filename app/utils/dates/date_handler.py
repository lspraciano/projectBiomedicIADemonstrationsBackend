from datetime import datetime

from fastapi import HTTPException, status


def validate_date_field(
        value: str,
        field_name: str,
        date_format: str
) -> datetime:
    """
    Validates a date field.

    Args:
        value: The value of the date field.
        field_name: The name of the date field.
        date_format: The format of the date field.

    Returns:
        A datetime object representing the date field, or None if the date field is not valid.

    Raises:
        HTTPException: If the date field is not valid.
    """
    try:
        date = datetime.strptime(
            value,
            date_format
        )
        return date
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name} is not valid"
        )
