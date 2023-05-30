#!/usr/bin/env python
# -*- coding: utf-8 -*-

from playingaround.spiders import crawling_spider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main():
    """ Main program """
    # Code goes over here.
    cspider = crawling_spider.CrawlingSpider()

    process = CrawlerProcess(get_project_settings())


    process.crawl(crawling_spider.CrawlingSpider)
    process.start()

    return 0

if __name__ == "__main__":

    main()