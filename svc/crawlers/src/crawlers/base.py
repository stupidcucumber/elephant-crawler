from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterator

from models import ScrappedText


class BaseCrawler(ABC):
    """Base class for crawlers.

    Parameters
    ----------
    name : str
        Name of the crawler.
    """

    def __init__(self, name: str, url: str) -> None:
        super(BaseCrawler, self).__init__()
        self.name = name
        self.url = url

    @abstractmethod
    def crawl(self) -> Iterator[ScrappedText]:
        """Crawls website.

        Returns
        -------
        Iterator[ScrappedText]
            An iterator that yields ScrappedText object. It
            returns None if no text left on the source provided.
        """
        raise NotImplementedError(
            "This method needs to be implemented in the child class"
        )

    def __iter__(self) -> Iterator[ScrappedText]:
        return self.crawl()
