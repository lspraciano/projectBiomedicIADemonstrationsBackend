from io import BytesIO

from PIL import Image


def image_to_bytes(
        image: Image
) -> bytes:
    """
    Converts a Pillow Image object to bytes.

    **Parameters**

    * **image** (Image): A Pillow Image object.

    **Returns**

    A bytes object containing the image data.
    """

    buff: BytesIO = BytesIO()
    image.save(buff, format="JPEG")
    return buff.getvalue()
