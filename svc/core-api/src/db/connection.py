import os
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from psycopg2 import connect
from psycopg2._psycopg import connection, cursor
from psycopg2.pool import ThreadedConnectionPool


def _extract_db_name_from_env() -> str | None:
    return os.getenv("DB_NAME")


def _extract_db_host_from_env() -> str:
    return os.getenv("DB_HOST")


def _extract_db_port_from_env() -> str:
    return os.getenv("DB_PORT")


def _extract_db_user_from_env() -> str:
    return os.getenv("DB_USER")


def _extract_db_password_from_env() -> str:
    return os.getenv("DB_PASSWORD")


@contextmanager
def db_cursor(dbpool: ThreadedConnectionPool) -> Iterator[cursor]:
    """Context manager to automate creating cursors from the pool of
    connections to the Postgres database.

    Parameters
    ----------
    dbpool : ThreadedConnectionPool
        Pool of connections to the Postgres DB.

    Yields
    ------
    cursor
        Cursor object to execute SQL queries.
    """
    conn: connection = dbpool.getconn()
    try:
        with conn.cursor() as cur:
            yield cur
            conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        dbpool.putconn(conn)


def setup_connection_pool(
    initialization_sql: Path | None = None,
) -> ThreadedConnectionPool:
    """Setups a connection pool for processing multiple queries.

    Parameters
    ----------
    initialization_sql : Path, optional
        If you want to pre-initialize database before usage (create tables, etc.) You can
        pass a path to the .sql file containing execution commands.

    Returns
    -------
    ThreadedConnectionPool

    Notes
    -----
    To run properly the following environment variables needs to be defined:
        - DB_NAME
        - DB_HOST
        - DB_PORT
        - DB_USER
        - DB_PASSWORD
    """
    _connection_pool = ThreadedConnectionPool(
        host=_extract_db_host_from_env(),
        port=_extract_db_port_from_env(),
        dbname=_extract_db_name_from_env(),
        user=_extract_db_user_from_env(),
        password=_extract_db_password_from_env(),
        minconn=4,
        maxconn=100,
    )

    if initialization_sql:
        with db_cursor(dbpool=_connection_pool) as cursor:
            cursor.execute(initialization_sql.read_text())

    return _connection_pool


def setup_connection() -> connection:
    """Setups a single connection to the Postgres database. Also runs initialization
    on a database.

    Returns
    -------
    connection
        A single connection to a database.

    Notes
    -----
    To run properly the following environment variables needs to be defined:
        - DB_NAME
        - DB_HOST
        - DB_PORT
        - DB_USER
        - DB_PASSWORD
    """
    _connection = connect(
        database=_extract_db_name_from_env(),
        user=_extract_db_user_from_env(),
        password=_extract_db_password_from_env(),
        host=_extract_db_host_from_env(),
        port=_extract_db_port_from_env(),
    )

    return _connection
