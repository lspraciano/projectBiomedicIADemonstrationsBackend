from typing import Dict

from pydantic import BaseModel


class ImageResponseSchema(BaseModel):
    """
    Schema for a response containing an image.

    **Attributes:**

    * **file_data:** The image data in bytes.
    """

    file_data: bytes


responseImage: Dict = {
    200: {
        "content": {
            "image/jpeg": {}
        },
        "description": "Return an image in body and the detections in headers",
    },
}
