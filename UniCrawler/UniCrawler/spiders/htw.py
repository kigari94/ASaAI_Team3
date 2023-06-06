import json
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field


# Item zur Ausgabe in der Konsole
# class myItem(Item):
#     # stud_url = Field()
#     # title = Field()
#     # paragraphs = Field()


class HtwSpider(CrawlSpider):
    name = "htw"
    allowed_domains = ["htw-dresden.de"]
    start_urls = ["https://www.htw-dresden.de"]

    rules = (
        Rule(LinkExtractor(allow="studium/vor-dem-studium/studienangebot"), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        # Nur zur Ausgabe in der Console nötig
        # item = myItem()
        # item["stud_url"] = response.url
        # item["title"] = response.xpath('//title/text()').get()
        # item["paragraphs"] = response.xpath('//p/text()').getall()
        # print(f"{response.url}")

        # writing scraped data into a dict to further progress
        data = dict()

        data['stud_url'] = response.url
        data['title'] = response.xpath('//title/text()').get()
        data['paragraphs'] = response.xpath('//p/text()').getall()

        # write data to json file
        with open('output.json', 'a') as f:
            json.dump(data, f)

        self.log('saved data to json')

        return print("test")
