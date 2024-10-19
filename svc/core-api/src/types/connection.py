from __future__ import annotations

from enum import StrEnum

from psycopg2 import OperationalError
from psycopg2._psycopg import cursor


class ConnectionStatus(StrEnum):
    """Helper class for providing info on connectivity to the database.

    Attributes
    ----------
    CONNECTION_SUCCESS : str, default="success"
        Connection with database is valid.
    CONNECTION_FAILED : str, default="fail"
        Connection with database is not valid.
    """

    CONNECTION_SUCCESS: str = "success"
    CONNECTION_FAILED: str = "fail"

    @staticmethod
    def check_connection(db_cursor: cursor) -> dict[str, ConnectionStatus]:
        """Checks connection with database.

        Parameters
        ----------
        db_cursor : cursor
            Cursor from the database.

        Returns
        -------
        dict[str, ConnectionStatus]
            Dict with key "db_connection" that provides info about
            the connection.
        """
        try:
            db_cursor.execute("SELECT 1;")
        except OperationalError:
            result = ConnectionStatus.CONNECTION_FAILED
        else:
            result = ConnectionStatus.CONNECTION_SUCCESS

        return {"db_connection": result}
