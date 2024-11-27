import os
from typing import override

from models import ScrappedText
from requests import Session


class CoreApiSession(Session):

    def _get_base_url(self) -> str:
        return f"http://{os.getenv("CORE_API_HOST")}:{os.getenv("CORE_API_PORT")}"

    @override
    def get(self) -> list[ScrappedText]:
        """Get all texts from the database.

        Returns
        -------
        list[ScrappedText]
            All scrapped texts.
        """
        response = super(CoreApiSession, self).get(
            url=self._get_base_url() + "/scrapped-texts"
        )
        return [ScrappedText(**item) for item in response.json()]

    @override
    def post(self, scrapped_text: ScrappedText) -> int:
        """Send post request to the CoreApi service.

        Parameters
        ----------
        scrappeed_text : ScrappedText
            Object to be inserted into the database.

        Returns
        -------
        int
            ID of the text inserted into the database.
        """
        response = super(CoreApiSession, self).post(
            url=self._get_base_url() + "/scrapped-text", json=scrapped_text.model_dump()
        )
        return response.json()
