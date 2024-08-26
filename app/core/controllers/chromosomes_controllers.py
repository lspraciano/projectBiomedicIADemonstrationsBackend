from typing import List, Optional, Dict, Tuple

from PIL import Image
from ultralytics import YOLO
from ultralytics.engine.results import Results

from app.core.machine_learning.results_handler.results_handler import get_plotted_image_from_result, \
    convert_result_to_dict


async def get_chromosomes_predictions(
        chromosomes_yolo_model: YOLO,
        image: Image,
) -> Optional[Tuple[Image, Dict]]:
    """
    Performs predictions of chromosomes images using a YOLO model.

    **Parameters**

    * **chromosome_yolo_model** (YOLO): A YOLO model trained to detect objects in chromosomes on images.
    * **image** (Image): The chromosomes image to be processed.

    **Returns**

    A tuple containing the processed image and the detection results, or `None`
    if no detections were made.
    """

    predict_result_list: List[Results] = chromosomes_yolo_model.predict(
        source=image,
        verbose=False,
        conf=0.5,
        imgsz=1152
    )

    predict_result: Results = next(iter(predict_result_list))

    image_from_array: Image = get_plotted_image_from_result(
        result=predict_result
    )

    result_dict: Dict = convert_result_to_dict(
        result=predict_result,
        classes=chromosomes_yolo_model.names
    )

    return image_from_array, result_dict
