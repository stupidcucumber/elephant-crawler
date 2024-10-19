from pathlib import Path

from fastapi import FastAPI
from models import ScrappedText
from src.db import db_cursor, insert_scrapped_text, setup_connection_pool
from src.types.connection import Connection

app = FastAPI()
db_connection_pool = setup_connection_pool(initialization_sql=Path("assets/init.sql"))


@app.get("/")
def health_check() -> dict[str, str]:
    return {"db_connection": Connection.CONNECTION_SUCCESS}


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
