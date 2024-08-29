import json
from typing import Dict, Optional

from PIL import Image
from fastapi import APIRouter, status, Depends
from fastapi.responses import StreamingResponse
from ultralytics import YOLO

from app.core.controllers.hematological_slides_controllers import get_hematological_slides_predictions
from app.core.controllers.processed_images_controllers import create_processed_image
from app.core.dependencies.images import open_valid_image_file
from app.core.dependencies.ml_models_loader import scanned_wbc_yolo_model_to_detection, \
    microscope_wbc_yolo_model_to_detection
from app.core.schemas.image_schemas import ImageResponseSchema, responseImage
from app.utils.images_handler.images_handler import image_to_bytes
from configuration.configs import settings

router = APIRouter(
    tags=["Hematological Slides"],
    prefix="/hematological-slides"
)


@router.post(
    path="/scanned-leukocytes/predict",
    response_class=StreamingResponse,
    response_model=ImageResponseSchema,
    responses=responseImage,
    status_code=status.HTTP_200_OK
)
async def hematological_wbc_scanned_slides_predict_(
        image: Image = Depends(open_valid_image_file),
        wbc_yolo_model: YOLO = Depends(scanned_wbc_yolo_model_to_detection)
):
    """
    **Hematological Scanned Leukocytes Slides Predict**

    This route performs detections of white blood cells in a scanned
    hematological slide image.
    """

    result_image: Optional[Image]
    result_dict: Optional[Dict]

    result_image, result_dict = await get_hematological_slides_predictions(
        wbc_yolo_model=wbc_yolo_model,
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


@router.post(
    path="/microscope-leukocytes/predict",
    response_class=StreamingResponse,
    response_model=ImageResponseSchema,
    responses=responseImage,
    status_code=status.HTTP_200_OK
)
async def hematological_wbc_microscope_slides_predict_(
        image: Image = Depends(open_valid_image_file),
        wbc_yolo_model: YOLO = Depends(microscope_wbc_yolo_model_to_detection)
):
    """
    **Hematological Microscope Leukocytes Slides Predict**

    This route performs detections of white blood cells in a optical microscope
    hematological slide image.
    """

    result_image: Optional[Image]
    result_dict: Optional[Dict]

    result_image, result_dict = await get_hematological_slides_predictions(
        wbc_yolo_model=wbc_yolo_model,
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
