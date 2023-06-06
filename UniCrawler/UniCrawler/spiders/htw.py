import json
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field


class myItem(Item):
    stud_url = Field()
    title = Field()
    paragraphs = Field()


class HtwSpider(CrawlSpider):
    name = "htw"
    allowed_domains = ["htw-dresden.de"]
    start_urls = ["https://www.htw-dresden.de"]

    rules = (
        Rule(LinkExtractor(allow="studium/vor-dem-studium/studienangebot"), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        item = myItem()
        item["stud_url"] = response.url
        item["title"] = response.xpath('//title/text()').get()
        item["paragraphs"] = response.xpath('//p/text()').getall()
        # url = response.xpath('//td[@id="additional_data"]/@href').get()

        # self.logger.info("This is an item page!", response.url)

        # yield {
        #     print("ich bin da"),
        #     print(f"{response.url}")
        # }
        # print(f"{response.url}")

        data = dict()

        data['stud_url'] = response.url
        data['title'] = response.xpath('//title/text()').get()
        data['paragraphs'] = response.xpath('//p/text()').getall()

        # write data to json file
        with open('output.json', 'a') as f:
            json.dump(data, f)

        self.log('saved data to json')

        return item



        # yield {
        #     "content": response.css(".intro span::text").get(),
        #     "content": response.text,
        #     "url": str(response.url)
        # }
        # print(f"url: {response.url}")