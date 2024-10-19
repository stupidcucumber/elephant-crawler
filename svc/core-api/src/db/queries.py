from models import ScrappedText
from psycopg2._psycopg import cursor


def insert_scrapped_text(db_cursor: cursor, scrapped_text: ScrappedText) -> int:
    """Function runs INSERT statement to add scrapped text to the DataBase.

    Parameters
    ----------
    db_cursor : cursor
        Cursor object to execute statements for the Postgres database.

    Returns
    -------
    int
        ID of the inserted row. Or -1 if statement failed.
    """
