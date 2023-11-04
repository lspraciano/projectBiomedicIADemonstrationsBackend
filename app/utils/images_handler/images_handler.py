from io import BytesIO

from PIL import Image


def image_to_bytes(
        image: Image
) -> bytes:
    """
    Converts an Image object to a bytes object.

    Args:
        image: The Image object to convert.

    Returns:
        A bytes object containing the image data.
    """
    buff: BytesIO = BytesIO()
    image.save(buff, format="JPEG")
    return buff.getvalue()

