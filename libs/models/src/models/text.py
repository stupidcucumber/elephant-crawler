from datetime import datetime

from pydantic import BaseModel, field_serializer


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

    link: str
    source: str
    lang: str
    author: str
    header: str
    scrapped_text: str
    date_added: str | datetime

    @field_serializer("date_added")
    @classmethod
    def _serialize_date_added(cls, date: str | datetime) -> str:
        if isinstance(date, datetime):
            return date.isoformat(sep=" ")
        return date
