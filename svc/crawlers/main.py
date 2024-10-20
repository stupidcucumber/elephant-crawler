import os

import requests
from src.crawlers import BaseCrawler
from src.network.connection import Connection


def main(crawlers: list[BaseCrawler]) -> None:

    connection = Connection(
        host=os.getenv(key="CORE_API_HOST"), port=os.getenv(key="CORE_API_PORT")
    )

    with requests.Session() as session:

        for crawler in crawlers:
            for scrapped_text in crawler:
                session.post(
                    url=connection.buildURL(endpoint="/scrapped-text"),
                    data=scrapped_text.model_dump(),
                )


if __name__ == "__main__":
    print("Found the following crawlers: ", BaseCrawler.__subclasses__())
    crawlers = [crawler() for crawler in BaseCrawler.__subclasses__()]

    try:
        main(crawlers=crawlers)
    except KeyboardInterrupt:
        print("User ended process.")
    else:
        print("Job is done.")
