from datetime import datetime

import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from scrapy.loader import ItemLoader


class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    subtitles = scrapy.Field()
    paragraphs = scrapy.Field()
    publication_date = scrapy.Field()
    url = scrapy.Field()


def remove_trailing_whitespace(input_string):
    return input_string.strip()


class ArticleLoader(ItemLoader):
    default_output_processor = TakeFirst()

    title_in = MapCompose(remove_trailing_whitespace)

    subtitles_in = MapCompose(remove_trailing_whitespace)
    subtitles_out = Join("\n")

    paragraphs_out = Join("\n")

    publication_date_in = MapCompose(datetime.fromisoformat)
