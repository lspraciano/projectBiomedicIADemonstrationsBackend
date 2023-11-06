from PIL import Image
from fastapi import UploadFile, HTTPException, status


async def open_valid_image_file(
        file: UploadFile,
):
    """
    Opens and validates an image file.

    **Parameters**

    * **file** (UploadFile): The image file to open and validate.

    **Returns**

    A Pillow Image object representing the image.

    **Raises**

    * **HTTPException**: If the file is not an image or if there is an error opening the file.
    """

    try:
        image: Image.Image = Image.open(file.file).convert("RGB")
        return image
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid file. The file must be an image."
        )
