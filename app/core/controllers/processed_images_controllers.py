from app.core.database.database import async_session
from app.core.models.processed_images_model import ProcessedImagesModel


async def create_processed_image(
        result: dict,
        route: str,
        image_data: bytes
) -> ProcessedImagesModel:
    """
    Creates a new ProcessedImagesModel instance with the specified route, result, and image data.

    **Parameters**

    * **result** (dict): The detection results.
    * **route** (str): The route that the image was processed on.
    * **image_data** (bytes): The image data in bytes.

    **Returns**

    A ProcessedImagesModel instance.
    """

    new_log: ProcessedImagesModel = ProcessedImagesModel(
        route=route,
        result=result,
        image_data=image_data
    )

    async with async_session() as session:
        session.add(new_log)
        await session.commit()
        await session.refresh(new_log)
        return new_log
