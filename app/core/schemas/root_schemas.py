from pydantic import BaseModel


class RootResponse(BaseModel):
    """
    Schema for the root response of the API.

    **Attributes:**

    * **status:** The status of the API.
    * **name:** The name of the API.
    * **version:** The version of the API.
    * **description:** A description of the API.
    * **authors:** A list of the authors of the API.
    * **documentation:** A link to the API documentation.
    """

    status: str
    name: str
    version: str
    description: str
    authors: list
    documentation: str

    class Config:
        from_attributes = True
