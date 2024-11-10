# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


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

    @classmethod
    def from_crawler(cls, crawler):
        """May be used to retrieve parameters from settings.py
        like this crawler.settings.get("SOME_SETTINGS_KEY")


        Parameters
        ----------
        crawler : Crawler
            The crawler, from which the items will be sent

        Returns
        -------
        SendItemToApiPipeline
        """
        return cls()

    def open_spider(self, spider):
        """May be used to establish connection with host"""
        pass

    def process_item(self, item, spider):
        """Send item data to api here"""
        return item
