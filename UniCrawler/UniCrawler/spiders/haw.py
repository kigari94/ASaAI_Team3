import scrapy
from scrapy.spiders import CrawlSpider


class CrawlingSpider(scrapy.Spider):
    name = "haw"
    allowed_domains = ["haw-hamburg.de"]
    start_urls = ["https://www.haw-hamburg.de/studium/studiengaenge-a-z/"]

    def parse(self, response):
        # Get name and url for all available courses
        courses = response.css('div.course_text')
        for course in courses:
            name = course.css('a::attr(title)').get()
            url = "https://www.haw-hamburg.de" + course.css('a::attr(href)').get()
            # Send request to get the respective course pages
            req = scrapy.Request(url, callback=self.parse_courses)
            req.meta['name'] = name
            req.meta['url'] = url
            yield req

    def parse_courses(self, response):
        # Extract required data from each course
        yield {
            'name': response.meta.get('name'),
            'url': response.meta.get('url'),
            'intro': response.css('span.intro::text').get(),
            'content': response.css('div.card-body.black p::text').getall(),
            'graduation': response.css('div.overview-content.col-12.col-sm-4.col-lg-12 div:nth-child(3)').get()
        }