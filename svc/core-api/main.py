from pathlib import Path

from fastapi import FastAPI
from models import ScrappedText
from src.db import db_cursor, insert_scrapped_text, setup_connection_pool
from src.types.connection import ConnectionStatus

app = FastAPI()
db_connection_pool = setup_connection_pool(initialization_sql=Path("assets/init.sql"))


@app.get("/", summary="Checks status of the connection to the Database.")
def health_check() -> dict[str, ConnectionStatus]:

    with db_cursor(dbpool=db_connection_pool) as cursor:
        result = ConnectionStatus.check_connection(db_cursor=cursor)

    return result


@app.post(
    "/scrapped-text",
    summary="""API endpoint for inserting scrapped text into a
    PostgreSQL database.
    """,
)
def post_scrapped_text(scrapped_text: ScrappedText) -> int:

    with db_cursor(dbpool=db_connection_pool) as cursor:
        inserted_scrapped_text_id = insert_scrapped_text(
            db_cursor=cursor, scrapped_text=scrapped_text
        )

    return inserted_scrapped_text_id
