from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider (CrawlSpider):
    name = "mycrawler"
    #allowed_domains = ["haw-hamburg.de"]
    #start_urls = ["https://www.haw-hamburg.de/"]
    allowed_domains = ["htw-dresden.de"]
    start_urls = ["https://www.htw-dresden.de/"]
    #allowed_domains = ["toscrape.com"]
    #start_urls = ["http://books.toscrape.com/"]


    rules = (
        #Rule(LinkExtractor(allow="studium/studiengaenge-a-z")),
        Rule(LinkExtractor(allow="studium/vor-dem-studium/studienangebot")),
        #Rule(LinkExtractor(allow="catalogue/category")),
    )

    def parse (self, response):

        print("processing:"+response.url)

        content = response.text
        url = response.url

        row_data=zip(content, url)

        for item in row_data:
            scraped_info = {
                'seite': item[0],
                'inhalt': item[1],
            }

            yield scraped_info





