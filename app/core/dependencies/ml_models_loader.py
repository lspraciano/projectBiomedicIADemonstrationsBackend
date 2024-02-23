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


async def microscope_wbc_yolo_model_to_detection() -> YOLO:
    """
    Loads the MICROSCOPE WBC YOLO model for detection.

    **Returns**

    A YOLO model loaded for detection.

    **Raises**

    * **HTTPException**: If the model could not be loaded.
    """

    yolo_model_name: str = "microscope_wbc_model"
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


async def scanned_wbc_yolo_model_to_detection() -> YOLO:
    """
    Loads the SCANNED WBC YOLO model for detection.

    **Returns**

    A YOLO model loaded for detection.

    **Raises**

    * **HTTPException**: If the model could not be loaded.
    """

    yolo_model_name: str = "scanned_wbc_model"
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


async def sperm_yolo_model_to_detection() -> YOLO:
    """
    Loads the SPERM YOLO model for detection.

    **Returns**

    A YOLO model loaded for detection.

    **Raises**

    * **HTTPException**: If the model could not be loaded.
    """

    yolo_model_name: str = "sperm_model"
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


async def melanoma_yolo_model_to_detection() -> YOLO:
    """
    Loads the MELANOMA YOLO model for detection.

    **Returns**

    A YOLO model loaded for detection.

    **Raises**

    * **HTTPException**: If the model could not be loaded.
    """

    yolo_model_name: str = "melanoma_model"
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


async def ki67_yolo_model_to_detection() -> YOLO:
    """
    Loads the KI67 YOLO model for detection.

    **Returns**

    A YOLO model loaded for detection.

    **Raises**

    * **HTTPException**: If the model could not be loaded.
    """

    yolo_model_name: str = "ki67_model"
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


async def blood_serum_yolo_model_to_detection() -> YOLO:
    """
    Loads the BLOOD_SERUM YOLO model for detection.

    **Returns**

    A YOLO model loaded for detection.

    **Raises**

    * **HTTPException**: If the model could not be loaded.
    """

    yolo_model_name: str = "blood_serum_model"
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


async def chromosomes_yolo_model_to_detection() -> YOLO:
    """
    Loads the CHROMOSOMES YOLO model for detection.

    **Returns**

    A YOLO model loaded for detection.

    **Raises**

    * **HTTPException**: If the model could not be loaded.
    """

    yolo_model_name: str = "chromosomes_model"
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
