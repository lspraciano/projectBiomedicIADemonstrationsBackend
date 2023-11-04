from typing import Dict, List

from PIL import Image
from numpy import ndarray
from ultralytics.engine.results import Results


def convert_result_to_dict(
        result: Results,
        classes: Dict
) -> Dict:
    """
    Converts a YOLOv8 Results object to a dictionary.

    Args:
        result: The YOLOv8 Results object to convert.
        classes: A dictionary mapping class IDs to class names.

    Returns:
        A dictionary containing the number of detections for each class.
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
    Generates a plotted image from a YOLOv8 Results object.

    Args:
        result: The YOLOv8 Results object to generate the plotted image from.

    Returns:
        A PIL Image object containing the plotted image.
    """
    predict_plotted_array: ndarray = result.plot()
    image_from_array: Image = Image.fromarray(predict_plotted_array[..., ::-1])
    return image_from_array
