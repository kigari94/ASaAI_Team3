import json
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field


class HtwSpider(CrawlSpider):
    name = "htw"
    allowed_domains = ["htw-dresden.de"]
    start_urls = ["https://www.htw-dresden.de"]

    rules = (
        Rule(LinkExtractor(allow="studium/vor-dem-studium/studienangebot"), callback="parse_item", follow=True),
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
        with open('htwoutput.json', 'a') as f:
            json.dump(self.content, f)



