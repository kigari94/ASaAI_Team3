#!/usr/bin/env python
# -*- coding: utf-8 -*-

from UniCrawler.spiders import htw
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from UniCrawler.spiders import htwk

def main():
    """ Main program """
    # Code goes over here.
    # cspider = crawling_spider.CrawlingSpider()

    process = CrawlerProcess(get_project_settings())

    process.crawl(htw.HtwSpider)
    process.start()

    return 0

if __name__ == "__main__":

    main()