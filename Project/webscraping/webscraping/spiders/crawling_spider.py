import scrapy
from scrapy.spiders import CrawlSpider


class CrawlingSpider(scrapy.Spider):
    name = "collegeCrawler"
    allowed_domains = ["haw-hamburg.de"]
    start_urls = ["https://www.haw-hamburg.de/studium/studiengaenge-a-z/"]

    def parse(self, response):
        titles = response.css('div.course_text')
        for title in titles:
            name = title.css('a::attr(title)').get()
            url = "https://www.haw-hamburg.de" + title.css('a::attr(href)').get()
            print(url)
            req = scrapy.Request(url, callback=self.parse_subcategory)
            req.meta['name'] = name
            yield req

    def parse_subcategory(self, response):
        yield {
            'name': response.meta.get('name'),
            'content': response.css('span.intro::text').get()
        }
