from typing import Optional

from fastapi import HTTPException, status
from ultralytics import YOLO

from app.core.machine_learning.ia_models.loader_ml_models import load_yolo_model


def raise_loader_exception(
        ml_model_name: str,
        task: str
) -> HTTPException:
    """
    Raises an HTTPException with the specified status code and detail message.

    **Parameters**

    * **ml_model_name** (str): The name of the ML model that could not be loaded.
    * **task** (str): The task that the ML model was being loaded for.

    **Returns**

    An HTTPException instance.
    """

    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=f"Could not load {ml_model_name} model to {task}"
    )


async def wbc_yolo_model_to_detection() -> YOLO:
    """
    Loads the WBC YOLO model for detection.

    **Returns**

    A YOLO model loaded for detection.

    **Raises**

    * **HTTPException**: If the model could not be loaded.
    """

    yolo_model_name: str = "wbc"
    task: str = "detection"

    yolo_model: Optional[YOLO] = load_yolo_model(
        yolo_model_name=yolo_model_name,
        task=task,
    )

    if not yolo_model:
        raise raise_loader_exception(
            ml_model_name=yolo_model_name,
            task=task,
        )

    return yolo_model
