import os
from typing import Optional

from ultralytics import YOLO

from app.core.machine_learning.ia_models.ml_models_path_structure import ml_models_dict_path_structure


def load_yolo_model(
        yolo_model_name: str,
        task: str,
) -> Optional[YOLO]:
    """
    Loads a YOLO model from the specified path.

    **Parameters**

    * **yolo_model_name** (str): The name of the YOLO model to load.
    * **task** (str): The task that the YOLO model will be used for.

    **Returns**

    A YOLO model object, or `None` if the model could not be loaded.
    """

    yolo_model_data: dict = ml_models_dict_path_structure[task][yolo_model_name]
    full_ml_model_path: str = f"{yolo_model_data['path']}/{yolo_model_data['weights_file_name']}"

    if not os.path.exists(full_ml_model_path):
        return None

    ml_classification_model: YOLO = YOLO(full_ml_model_path)

    return ml_classification_model
