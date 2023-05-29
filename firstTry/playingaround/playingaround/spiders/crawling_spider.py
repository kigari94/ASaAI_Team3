from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider (CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["htw-dresden.de"]
    start_urls = ["https://www.htw-dresden.de/"]
    #allowed_domains = ["toscrape.com"]
    #start_urls = ["http://books.toscrape.com/"]


    rules = (
        Rule(LinkExtractor(allow="studium/vor-dem-studium/studienangebot")),
        #Rule(LinkExtractor(allow="catalogue/category")),
    )
