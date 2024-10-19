from itertools import chain

from models import ScrappedText
from psycopg2._psycopg import cursor
from pydantic import BaseModel


def _sql_values_from_model(
    model: BaseModel, **additional_kwargs
) -> tuple[list[str], list[str]]:
    """Extracts keys and values from the model.

    Parameters
    ----------
    model : BaseModel
        Model that needs to be sliced into keys and values.

    Returns
    -------
    tuple[list[str], list[str]]
        A tuple of list of keys and corresponding values.
    """
    result_keys = []
    result_values = []
    for key, value in chain(model.model_dump().items(), additional_kwargs.items()):
        result_keys.append(key)
        result_values.append(value)
    return (result_keys, result_values)


def insert_scrapped_text(
    db_cursor: cursor, scrapped_text: ScrappedText, **kwargs
) -> int:
    """Function runs INSERT statement to add scrapped text to the DataBase.

    Parameters
    ----------
    db_cursor : cursor
        Cursor object to execute statements for the Postgres database.
    scrapped_text : ScrappedText
        BaseModel inherited object that will be inserted into the database.
    **kwargs
        Additional arguments that will be considered as columns to the
        database table.

    Returns
    -------
    int
        ID of the inserted row. Or -1 if statement failed.
    """

    keys, values = _sql_values_from_model(model=scrapped_text, **kwargs)

    db_cursor.execute(
        f"""
        INSERT INTO scrapped_texts ({','.join(keys)})
        VALUES ({",".join(["%s"] * len(keys))})
        RETURNING id;
        """,
        values,
    )

    return db_cursor.fetchone()[0]
