import json
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field


class UlSpider(CrawlSpider):
    name = "ul"
    allowed_domains = ["uni-luebeck.de"]
    start_urls = ["https://www.uni-luebeck.de"]

    rules = (
        Rule(LinkExtractor(allow="studium"), callback="parse_item", follow=True),
        Rule(LinkExtractor(allow="studium/studiengaenge"), callback="parse_item", follow=True),
    )

    content = list()

    def parse_item(self, response):

        # writing scraped data into a dict to further progress
        data = dict()

        data['stud_url'] = response.url
        data['title'] = response.xpath('//title/text()').get()
        data['paragraphs'] = response.xpath('//p/text()').getall()

        self.add_item_to_list(data)

        return None

    def add_item_to_list(self, item):
        self.content.append(item)

    def write_json(self):
        with open('Resources/uloutput.json', 'w') as f:
            json.dump(self.content, f)



