from typing import Dict, List

from PIL import Image
from numpy import ndarray
from ultralytics.engine.results import Results


def convert_result_to_dict(
        result: Results,
        classes: Dict
) -> Dict:
    """
    Converts a YOLO detection result to a dictionary.

    **Parameters**

    * **result** (Results): A YOLO detection result.
    * **classes** (Dict): A dictionary mapping class IDs to class names.

    **Returns**

    A dictionary mapping class names to counts.
    """

    counts: Dict = {}
    detected_classes: List[float] = result.boxes.cls.tolist()

    for class_id in detected_classes:
        class_name: str = classes[int(class_id)]
        if class_name not in counts:
            counts[class_name] = 0
        counts[class_name] += 1

    return counts


def get_plotted_image_from_result(
        result: Results
) -> Image:
    """
    Converts a YOLO detection result to a Pillow Image object.

    **Parameters**

    * **result** (Results): A YOLO detection result.

    **Returns**

    A Pillow Image object containing the detections.
    """

    predict_plotted_array: ndarray = result.plot()
    image_from_array: Image = Image.fromarray(predict_plotted_array[..., ::-1])
    return image_from_array
