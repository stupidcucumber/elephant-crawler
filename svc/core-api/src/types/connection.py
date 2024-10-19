from enum import StrEnum

from psycopg2._psycopg import connection


class Connection(StrEnum):
    CONNECTION_SUCCESS: str = "success"
    CONNECTION_FAILED: str = "fail"

    @staticmethod
    def check_connection(db_connection: connection) -> "Connection":
        return db_connection.info.status
