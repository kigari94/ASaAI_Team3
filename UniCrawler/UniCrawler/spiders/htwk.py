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


class HtwkSpider(CrawlSpider):
    name = "htwk"
    allowed_domains = ["htwk-leipzig.de"]
    start_urls = ["https://www.htwk-leipzig.de"]

    rules = (
        Rule(LinkExtractor(allow="studieren/studiengaenge"), callback="parse_item", follow=True),
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
        with open('htwkoutput.json', 'a') as f:
            json.dump(data, f)

        self.log('saved data to json')

        return print("saved a page")
