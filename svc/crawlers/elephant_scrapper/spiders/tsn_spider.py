from datetime import datetime, timedelta

import scrapy
from elephant_scrapper.items import ArticleItem, ArticleLoader
from scrapy import signals
from scrapy.exceptions import DontCloseSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TsnSpider(CrawlSpider):
    name = "tsn.ua"
    allowed_domains = ["tsn.ua"]

    def __init__(self, *args, **kwargs):
        super(TsnSpider, self).__init__(*args, **kwargs)
        self.date_to_process = datetime.now()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(TsnSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.idle_handler, signal=signals.spider_idle)

        return spider

    rules = (
        Rule(LinkExtractor(allow=r"news/page-*")),
        Rule(LinkExtractor(restrict_css="a.c-card__link"), callback="parse_item"),
    )

    def start_requests(self):
        yield scrapy.Request(url=self._build_next_date_query())

    def parse_item(self, response):
        article_loader = ArticleLoader(item=ArticleItem(), response=response)
        article_loader.add_css("title", "h1.c-card__title span::text")
        article_loader.add_css("subtitles", "div.c-article__lead p strong::text")
        article_loader.add_css("subtitles", "div[data-content] h2 strong::text")
        article_loader.add_css("author", "dd span.c-bar__spacer-l::text")
        article_loader.add_value(
            "paragraphs",
            response.xpath("//div[@data-content]//p").xpath("string()").getall(),
        )
        article_loader.add_value("url", response.url)
        article_loader.add_value("source", "tsn.ua")
        article_loader.add_value("language", "ua")
        article_loader.add_css(
            "publication_date",
            "h1 + footer.c-card__foot dl dd.c-bar__label time::attr(datetime)",
        )
        return article_loader.load_item()

    def idle_handler(self):
        url = self._build_next_date_query()
        request = scrapy.Request(url=url)
        self.crawler.engine.crawl(request)

        raise DontCloseSpider

    def _build_next_date_query(self):
        self.date_to_process = self.date_to_process - timedelta(days=1)
        return self.date_to_process.strftime(
            "https://tsn.ua/news?day=%d&month=%m&year=%Y"
        )
