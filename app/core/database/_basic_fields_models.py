from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_mixin, declared_attr
from sqlalchemy.sql import func


@declarative_mixin
class CommonFields:
    @declared_attr
    def last_change(cls):
        """
        Creates a `DateTime` column with the `timezone=True`, `nullable=False`,
        `server_default=func.now()`, and `onupdate=func.now()` flags.

        This ensures that the column will store the date and time in
        the database in the correct time zone, that the column cannot be null,
        and that the column is automatically updated with the current timestamp
         whenever the model is saved or updated.

        Returns:
            A `DateTime` column with the specified flags.
        """
        return Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
