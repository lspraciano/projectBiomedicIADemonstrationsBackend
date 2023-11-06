from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_mixin, declared_attr
from sqlalchemy.sql import func


@declarative_mixin
class CommonFields:
    @declared_attr
    def last_change(cls):
        """Safely creates a `last_change` field for SQLAlchemy models.

        The `last_change` field is a DateTime field that is automatically updated whenever the model
        is changed. This can be useful for tracking when models were last updated.

        **Returns**

        A Column object representing the `last_change` field.
        """

        return Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
