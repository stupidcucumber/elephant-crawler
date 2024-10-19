from pydantic import BaseModel


class ScrappedText(BaseModel):
    """Wrapper class for the text that
    crawler found.

    Attributes
    ----------
    text : str
        Text itself.
    """

    text: str
