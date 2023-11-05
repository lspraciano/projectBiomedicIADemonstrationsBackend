from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database.database import ModelBase


class ProcessedImages(ModelBase):
    __tablename__: str = "processed_images"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    route: Mapped[str] = mapped_column(String, nullable=False)
