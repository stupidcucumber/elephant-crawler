# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from datetime import datetime

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from models import ScrappedText
from scrapy.exceptions import DropItem

from .request_sender import CoreApiSession


class FilterImcompleteDataPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if not adapter.get("url"):
            raise DropItem("Missing url")

        required_props = ["title", "paragraphs", "publication_date"]
        for prop in required_props:
            if not adapter.get(prop):
                raise DropItem(f"Missing {prop} in {adapter.get("url")}")

        return item


class SendItemToApiPipeline:
    def __init__(self):
        super().__init__()
        self.session = CoreApiSession()

    def process_item(self, item, spider):
        """Send item data to api here"""
        adapter = ItemAdapter(item)

        new_text = ScrappedText(
            link=adapter.get("url"),
            source=adapter.get("source"),
            lang=adapter.get("language"),
            author=adapter.get("author"),
            header=adapter.get("title"),
            scrapped_text=adapter.get("paragraphs"),
            date_added=datetime.now(),
        )

        self.session.post(new_text)
        return item
