import json
from typing import Dict, Optional

from PIL import Image
from fastapi import APIRouter, status, Depends
from fastapi.responses import StreamingResponse
from ultralytics import YOLO

from app.core.controllers.melanoma_controllers import get_melanoma_predictions
from app.core.controllers.processed_images_controllers import create_processed_image
from app.core.dependencies.images import open_valid_image_file
from app.core.dependencies.ml_models_loader import melanoma_yolo_model_to_detection
from app.core.schemas.image_schemas import ImageResponseSchema, responseImage
from app.utils.images_handler.images_handler import image_to_bytes

router = APIRouter(
    tags=["Melanoma"],
    prefix="/melanoma"
)


@router.post(
    path="/predict",
    response_class=StreamingResponse,
    response_model=ImageResponseSchema,
    responses=responseImage,
    status_code=status.HTTP_200_OK
)
async def melanoma_predict_(
        image: Image = Depends(open_valid_image_file),
        melanoma_yolo_model: YOLO = Depends(melanoma_yolo_model_to_detection)
):
    """
    **Blood Serum Predict**

    This route performs detections of melanoma in skin image.
    """

    result_image: Optional[Image]
    result_dict: Optional[Dict]

    result_image, result_dict = await get_melanoma_predictions(
        melanoma_model=melanoma_yolo_model,
        image=image
    )

    response: StreamingResponse = StreamingResponse(
        content=iter([image_to_bytes(result_image)]),
        media_type=f"image/{result_image.format}"
    )

    response.headers["Detections"]: str = json.dumps(result_dict)

    await create_processed_image(
        result=result_dict,
        route=router.prefix,
        image_data=image_to_bytes(result_image)
    )

    return response
