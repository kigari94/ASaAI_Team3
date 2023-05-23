from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "collegeCrawler"
    allowed_domains = ["haw-hamburg.de"]
    start_url = ["https://www.haw-hamburg.de/"]