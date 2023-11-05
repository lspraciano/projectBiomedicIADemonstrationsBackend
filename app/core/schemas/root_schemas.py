from pydantic import BaseModel


class RootResponse(BaseModel):
    """
    Represents the response of a health check.

    Attributes:
        status: The status status of the project.
        name: The name of the project.
        version: The version of the project.
        description: The description of the project.
        authors: The authors of the project.
        documentation: The path to documentation of the project.
    """
    status: str
    name: str
    version: str
    description: str
    authors: list
    documentation: str

    class Config:
        from_attributes = True
