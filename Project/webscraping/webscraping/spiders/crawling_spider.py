from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name = "collegeCrawler"
    allowed_domains = ["haw-hamburg.de"]
    start_urls = ["https://www.haw-hamburg.de/"]

    rules = (
        Rule(LinkExtractor(allow="studium/studiengaenge-a-z/")),
        Rule(LinkExtractor(allow="courses/show", deny=("termine/-schulcampus", "termin", "emil", "elearning")), callback="parse_item"),
    )

    def parse_item(self, response):
        yield {
            "content": response.css(".intro span::text").get(),
            "url": str(response.url)
        }