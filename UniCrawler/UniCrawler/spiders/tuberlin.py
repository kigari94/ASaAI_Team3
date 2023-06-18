import json
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field


class TuBerlinSpider(CrawlSpider):
    name = "tuberlin"
    allowed_domains = ["tu.berlin"]
    start_urls = ["https://www.tu.berlin"]

    rules = (
        Rule(LinkExtractor(allow="studieren/studienangebot/gesamtes-studienangebot"), callback="parse_item", follow=True),
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
        with open('Resources/tuberlinoutput.json', 'w') as f:
            json.dump(self.content, f)



