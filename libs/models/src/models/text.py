from pydantic import BaseModel


class ScrappedText(BaseModel):
    """Wrapper class for the text that
    crawler found.

    Attributes
    ----------
    scrapped_text : str
        Text itself.
    date_added : str
        Datetime parsed object that corresponds to the date when
        text was found.
    """

    scrapped_text: str
    date_added: str
