import json
from typing import Dict, Optional

from PIL import Image
from fastapi import APIRouter, status, Depends
from fastapi.responses import StreamingResponse
from ultralytics import YOLO

from app.core.controllers.processed_images_controllers import create_processed_image
from app.core.controllers.sperm_controllers import get_sperm_predictions
from app.core.dependencies.images import open_valid_image_file
from app.core.dependencies.ml_models_loader import sperm_yolo_model_to_detection
from app.core.schemas.image_schemas import ImageResponseSchema, responseImage
from app.utils.images_handler.images_handler import image_to_bytes
from configuration.configs import settings

router = APIRouter(
    tags=["Sperm"],
    prefix="/sperm"
)


@router.post(
    path="/predict",
    response_class=StreamingResponse,
    response_model=ImageResponseSchema,
    responses=responseImage,
    status_code=status.HTTP_200_OK
)
async def sperm_predict_(
        image: Image = Depends(open_valid_image_file),
        sperm_yolo_model: YOLO = Depends(sperm_yolo_model_to_detection)
):
    """
    **Sperm Predict**

    This route performs detections of sperm in image.
    """

    result_image: Optional[Image]
    result_dict: Optional[Dict]

    result_image, result_dict = await get_sperm_predictions(
        sperm_yolo_model=sperm_yolo_model,
        image=image
    )

    response: StreamingResponse = StreamingResponse(
        content=iter([image_to_bytes(result_image)]),
        media_type=f"image/{result_image.format}"
    )

    response.headers["Detections"]: str = json.dumps(result_dict)

    if settings.SAVE_PREDICTION:
        await create_processed_image(
            result=result_dict,
            route=router.prefix,
            image_data=image_to_bytes(result_image)
        )

    return response
