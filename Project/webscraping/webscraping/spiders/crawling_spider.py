import scrapy
from scrapy.spiders import CrawlSpider


class CrawlingSpider(scrapy.Spider):
    name = "collegeCrawler"
    allowed_domains = ["haw-hamburg.de"]
    start_urls = ["https://www.haw-hamburg.de/studium/studiengaenge-a-z/"]

    def parse(self, response):
        titles = response.css('div.course_text')
        for title in titles:
            yield {
                'title': title.css('a::attr(title)').get(),
                'url': "https://www.haw-hamburg.de" + title.css('a::attr(href)').get()
                # "url": str(response.request.url),
            }
            # yield item
        #     yield {
        #         "url": str(response.request.url),
        #
        #         # "title": response.css('td.sorting_1 a.smoothState::text').get(),
        #         "title": response.xpath('//*[@id="course_table"]/tbody/tr[1]/td[1]/a/text()').get(),
        #
        #     # "content": response.css(".intro span::text").get(),
        #     # "status": str(response.status),
        #     # "Test": "Test"
        # }
        # for text in response.xpath('//*[@id="p85"]'):
        #     yield {
        #         "Test": "Test",
        #         "Text": text.xpath('//*[@id="c2561"]/p[2]/text()[1]')
        #     }
