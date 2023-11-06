from sqlalchemy import Integer, String, LargeBinary, JSON
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database.database import ModelBase


class ProcessedImagesModel(ModelBase):
    __tablename__: str = "processed_images"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    result: Mapped[JSON] = mapped_column(JSON, nullable=False)
    route: Mapped[str] = mapped_column(String, nullable=False)
    image_data: Mapped[bytes] = mapped_column(LargeBinary(length=4056), nullable=False)
