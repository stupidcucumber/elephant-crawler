from pydantic import BaseModel


class ScrappedText(BaseModel):
    """Wrapper class for the text that
    crawler found.

    Attributes
    ----------
    scrapped_text : str
        Text itself.
    """

    scrapped_text: str
