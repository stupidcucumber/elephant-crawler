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


class TieAdditionalAttributesPipeline:
    def process_item(self, item, spider):
        # setting additional attributes
        return item


class SaveToDbPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        # just an example to fetch parameter from outside
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE", "items"),
        )

    def open_spider(self, spider):
        # launch db
        pass

    def close_spider(self, spider):
        # close db
        pass

    def process_item(self, item, spider):
        # saving item to database
        return item
